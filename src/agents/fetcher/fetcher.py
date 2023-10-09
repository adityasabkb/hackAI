from uagents import Agent,Context
from utils import get_rate
from messages import *

fetcher = Agent(name="Fetcher Agent")

@fetcher.on_message(FetchRequest,replies={FetchResponse})
async def fetch_rates(ctx: Context,sender: str,msg: FetchRequest):
    '''
    this function defines behaviour of fetcher agent when a fetch request is recieved from client
    '''

    try:
        #try to fetch rates and send to client
        rates = get_rate(msg.secondary_currencies,msg.base_currency)
        await ctx.send(sender, FetchResponse(success=True,rates=rates))
    except:
        #send message with success=False in case errors occured while fetching data
        ctx.send(sender,FetchResponse(success=False,rates={}))
    
