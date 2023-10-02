from uagents import Model

class FetchRequest(Model):
    base_currency: str
    secondary_currencies: list

class FetchResponse(Model):
    rates: dict

