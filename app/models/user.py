from sqlmodel import SQLModel, Field, UniqueConstraint
from typing import Optional

class User(SQLModel, table=True):
    __table_args__ = (UniqueConstraint("username"), UniqueConstraint("email"))
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    email: str
    hashed_password: str
