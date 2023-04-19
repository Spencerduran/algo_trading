#from polygon.websocket import WebSocketClient
#from polygon.websocket.models import WebSocketMessage
#from typing import List
#from dotenv import load_dotenv
#import os
#
#load_dotenv()
#api_key = os.getenv('ENV_KEY')
#
#
#def establish_websocket_client(api_key) -> None:
#    """
#    For the websocket client polygon, with the API key
#    :return: None
#    """
#    try:
#        websocket_client = WebSocketClient(api_key)
#        print("Polygon Websocket connection established")
#    except (ValueError, ConnectionRefusedError, ConnectionError):
#        print(f"Polygon Websocket connection not established, with error: {e}")
#establish_websocket_client(api_key)
import time
from typing import List

from polygon.websocket import WebSocketClient
from polygon import STOCKS_CLUSTER


def my_custom_process_message(messages: List[str]):
    def add_message_to_list(message):
        messages.append(message)

    return add_message_to_list


def main():
    key = 'your api key'
    messages = []
    my_client = WebSocketClient(STOCKS_CLUSTER, key, my_custom_process_message(messages))
    my_client.run_async()

    my_client.subscribe("T.MSFT", "T.AAPL", "T.AMD", "T.NVDA")
    time.sleep(1)

    my_client.close_connection()
    
    for message in messages:
        # process messages
        pass


if __name__ == "__main__":
    main()
