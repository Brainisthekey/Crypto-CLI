from pydantic import BaseModel

class ShowCandles(BaseModel):
    symbol : str
    price : str

class GetAccount(BaseModel):
    pass