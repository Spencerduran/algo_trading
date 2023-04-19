import datetime
import json
import os
import time

import requests
from flask import Flask, request

#------------------------- TRADE STATION CLIENT --------------------------
class TradingBot:
    def __init__(self, client_id, client_secret, refresh_token, account_id):
        self.client_id = client_id
        self.client_secret = client_secret
        self.refresh_token = refresh_token
        self.account_id = account_id
        self.access_token = None
        self.token_expiration_time = None
        self.authenticate()

    def authenticate(self):
        token_url = "https://signin.tradestation.com/oauth/token"
        payload = {
            "grant_type": "refresh_token",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "refresh_token": self.refresh_token,
        }
        headers = {"content-type": "application/x-www-form-urlencoded"}
        response = requests.post(token_url, headers=headers, data=payload)
        response_data = json.loads(response.text)
        self.access_token = response_data["access_token"]
        expires_in = response_data["expires_in"]
        self.token_expiration_time = time.time() + expires_in - 60  # Subtracting 60 seconds for safety

    def is_token_expired(self):
        return time.time() > self.token_expiration_time

    def send_trade(self, symbol: str, quantity: int=1, action:str="BUY", price : float=0.0, duration : str='DAY', route: str=None):
        if self.is_token_expired():
            self.authenticate()
        # Can be simulation or real environment
        trade_url = f'{BASE_URL}/orderexecution/orders'  
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json",
        }
        payload = {
            "AccountID" : self.account_id,
            "Symbol": symbol,
            "Quantity": f"{quantity}",
            "TradeAction" : action.upper(),
            "TimeInForce": {"Duration": duration.upper()}
        }  
        if price == 0.0:
          payload["OrderType"] = "Market"
        else:
          payload["OrderType"] = "Limit"
          payload["LimitPrice"] = f"{price}"
        if route:
          payload["Route"] = route
        response = requests.post(trade_url, headers=headers, data=json.dumps(payload))
        return response

#------------------------- CONFIGURATION --------------------------# Constants
DT_FORMAT = '%m/%d/%Y %I:%M:%S %p'

# Flask app setup
app = Flask(__name__)

# Config setup
CONFIG_PATH = 'config.json'
with open(CONFIG_PATH, 'r') as f:
    CONFIG = json.load(f)

BASE_URL = 'https://sim-api.tradestation.com/v3' if CONFIG['simulation_mode'] else 'https://api.tradestation.com/v3'bot = None

#------------------------- APP -------------------------------------
def log_msg(message):
    with open(CONFIG['log_path'], 'a') as log_f:
        log_f.write(f'{datetime.datetime.now().strftime(DT_FORMAT)} - {message}\n')

@app.route('/webhook', methods=['POST'])
def webhook():
    # Capture the webhook then place the order
    if request.method == 'POST':
        data = request.json
        log_msg('Webhook received, placing order...')
        place_order(data)


# Webhook Example:
# 'action' must be:
# BUY - crypto, equities and futures
# SELL - crypto, equities and futures  
#    
# {
#    "symbol": "TSLA",
#    "action" : "BUY",
#    "price": 100.05    
# }
#
# For Market Orders
#
# {
#    "symbol": "TSLA",
#    "action" : "SELL"   
# } 
def place_order(data):
    global bot

    # Setup trading bot
    if not bot:
        ts = CONFIG['trade_station']
        bot = TradingBot(ts['client_id'], ts['client_secret'], ts['refresh_token'], ts['account_id'])

    order = CONFIG['order_details']
    response = bot.send_trade(
        # From webhook
        symbol    = data['symbol'],
        action    = data['action'],
        price     = float(data.get('price', 0)), #Could be null
        # From configuration,
        quantity  = int(order.get('quantity', 1)), #Could be null
        duration  = order.get('duration', "DAY"),
        route     = order.get('route', None)
    )

    if response.ok:
        log_msg(f'Order successfully placed for {data["symbol"]}. Details: {response.json()}')
    else:
        log_msg(f'Order placement failed for {data["symbol"]} with status code {response.status_code}.') 
        log_msg(f'Error details: {response.json()}')

if __name__ == '__main__':
    log_msg('Starting app and waiting for messages...')
    app.run()