from datetime import datetime
from enum import Enum
from uuid import UUID

from pydantic import BaseModel, Field


class Type(Enum):
    INCOME = "income"
    EXPENSE = "expense"


class TransactionCreate(BaseModel):
    amount: float = Field(gt=0)
    category_id: UUID | None = None
    date: datetime = Field(default_factory=datetime.now)
    description: str | None = Field(None, max_length=1000)


class TransactionRead(TransactionCreate):
    id: str

# class Categories:
#     id: int
#     type: Type
#
#
# asd = Categories()
# asd.type = Type.INCOME