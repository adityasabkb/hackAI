from agents import fetcher,test_client
from uagents import Bureau


DEBUG_FETCHER = True

if DEBUG_FETCHER:
    b = Bureau()
    b.add(fetcher)
    b.add(test_client)
    b.run()
