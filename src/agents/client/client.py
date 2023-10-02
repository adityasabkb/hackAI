from uagents import Agent,Context
from messages import *
from utils import convert
from agents.fetcher import fetcher


base_currency = input("Enter Base USD  : ")
secondary_currencies = input("Enter Secondary 'JPY INR EUR'  : ")
threshold = input("Enter Threshold 20 75 19 : ")

secondary_currencies, threshold = convert(secondary_currencies, threshold)

client = Agent(name="Clinet Agent")

@client.on_interval(period=3600.0, messages= FetchRequest)
async def fetch_rates(ctx: Context):
    await ctx.send(fetcher.address, FetchRequest(base_currency=base_currency, secondary_currencies=secondary_currencies)
)

@client.on_message(FetchResponse)
async def print_rates(ctx: Context,_sender: str, msg: FetchResponse):
    ctx.logger.info(f"rates are: {msg.rates}")
    
    for i in msg.rates.keys():
        if msg.rates[i] >= threshold[i]:
            ctx.logger.critical(f"ALERT!! {i} is crossing threshold {threshold[i]}")
            

    