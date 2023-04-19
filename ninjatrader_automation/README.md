# karma_bot

# Getting Started

This bot requires a a few things to build out. You need the following:

- Karma Algo
- Pipedream account
- Discord Server
- Discord Bot
- NinjaTrader (or any trade platfor, if we really thing about it, that suppports hotkeys)
- Python with *list of requierments*

# Discord Config 

To get started, in a server where you have admin permissions, create a channel, for the case of this read me I will refer to as *#alert-channel* and configure a webhook bot for it. Note this you will need it later. 

# Discord Bot Config

Create a discord bot and add it to your server. It at minimum it needs to be able to read and send messages. Create a token and set aside, you will need it later. 

# Pipedream Config Part 1

Create a pipedream account and create a new workflow with a trigger on inbound HTTP requests. Copy this Web address and lets continue after TradingView Setup

# TradingView Config

On a 15 Secong NQ Chart (so we generate an event quickly), add the Karma Algo with OPEN LONG, OPEN SHORT, CLOSE LONG, CLOSE SHORT and TAKE PROFIT alerts and features enabled. Create an alert (recommend shortening the Alert Name to NQ Alert) and in the notifications tab, in the webhook paste in the URL you got from pipedream. Now wait a minute or two for an alert to be triggered, then return to pipedream. 

# Pipedream Config 2

You should now be able to select an event in pipedream workflow, in the next step, select python and insert this code, with the webhook URL you saved earlier.

```
from discord_webhook import DiscordWebhook

def handler(pd: "pipedream"):
  # Reference data from previous step
  output = pd.steps["trigger"]["event"]["body"]
  webhook = DiscordWebhook(url='the webhook url from discord server in these quotes', content=output)
  response = webhook.execute()
```

Test and you should now see a message in your *#alert-channel*

# Python on trade computer
