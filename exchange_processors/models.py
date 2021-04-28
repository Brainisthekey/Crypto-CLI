from pydantic import BaseModel

class ShowCandles(BaseModel):
    symbol : str
    interval : str
