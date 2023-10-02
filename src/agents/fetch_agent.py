
from uagents import Agent,Context
from utils import get_rate
import os
from messages import *

EXCHANGE_RATE_API = os.environ.get("EXCHANGE_RATE_API")



fetcher = Agent(name="Fetcher Agent", seed=EXCHANGE_RATE_API)

@fetcher.on_message(FetchRequest,replies={FetchResponse})
async def fetch_rates(ctx: Context,sender: str,msg: FetchRequest):
    rates = get_rate(msg.secondary_currencies,msg.base_currency)
    rates = FetchResponse(rates=rates)
    return rates
