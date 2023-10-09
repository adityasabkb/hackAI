from uagents import Agent,Context
from utils import get_rate
from messages import *

fetcher = Agent(name="Fetcher Agent")

@fetcher.on_message(FetchRequest,replies={FetchResponse})
async def fetch_rates(ctx: Context,sender: str,msg: FetchRequest):
    try:
        rates = get_rate(msg.secondary_currencies,msg.base_currency)
        await ctx.send(sender, FetchResponse(success=True,rates=rates))
    except:
        ctx.send(sender,FetchResponse(success=False,rates={}))
    
