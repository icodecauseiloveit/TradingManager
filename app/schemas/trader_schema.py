from pydantic import BaseModel
from typing import Optional

class TraderCreate(BaseModel):
    balance: float

class TraderRead(BaseModel):
    id: int
    balance: float

class TraderUpdate(BaseModel):
    balance: Optional[float]
