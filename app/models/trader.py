from sqlmodel import SQLModel, Field
from typing import Optional

class Trader(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    balance: float
