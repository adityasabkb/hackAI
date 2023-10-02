
from uagents import Agent,Context

import os
from messages import *
from utils import get_rate
EXCHANGE_RATE_API = os.environ.get("EXCHANGE_RATE_API")



fetcher = Agent(name="Fetcher Agent", seed=EXCHANGE_RATE_API)

@fetcher.on_message(FetchRequest,replies={FetchResponse})
async def fetch_rates(ctx: Context,sender: str,msg: FetchRequest):
    rates = get_rate(msg.secondary_currencies,msg.base_currency)
    rates = FetchResponse(rates=rates)
    await ctx.send(sender,rates)


test_client = Agent(name="test client")

@test_client.on_interval(period=10.0,messages=FetchRequest)
async def send_request(ctx: Context):
    await ctx.send(fetcher.address, FetchRequest(base_currency="USD", secondary_currencies=["INR","AED"]))

@test_client.on_message(FetchResponse,replies=set([]))
async def print_rates(ctx: Context,_sender: str, msg: FetchResponse):
    ctx.logger.info(f"rates are: {msg.rates}")