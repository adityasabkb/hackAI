from uagents import Model
from typing import Union
class FetchRequest(Model):
    base_currency: str
    secondary_currencies: Union(str,list,tuple)

class FetchResponse(Model):
    rates: dict