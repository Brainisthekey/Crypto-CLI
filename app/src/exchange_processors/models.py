from pydantic import BaseModel

class ShowCandles(BaseModel):
    symbol: str
    price: str
class PlaceOrder(BaseModel):
    pass

class GetAccount(BaseModel):
    balances : dict
