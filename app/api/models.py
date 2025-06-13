from pydantic import BaseModel, Field
from typing import List


class Expense(BaseModel):
    id: int
    description: str
    amount: float = Field(gt=0)
    # currency: str | None


class Expenses(BaseModel):
    expenses: List[Expense]
