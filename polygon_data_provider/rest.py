from datetime import datetime as d
from polygon.rest import RESTClient
from typing import cast
from urllib3 import HTTPResponse
from dotenv import load_dotenv
import os

load_dotenv()

POLYGON_API_KEY = os.getenv('ENV_KEY')
date = d.now()

client = RESTClient(POLYGON_API_KEY)

aggs = cast(
    HTTPResponse,
    client.get_aggs(
        "AAPL",
        5,
        "day",
        "2022-06-22",
        "2022-06-23",
        raw=True,
    ),
)
print(date.strftime("%Y-%m-%d %H:%M:%S"))
print(aggs.data)
