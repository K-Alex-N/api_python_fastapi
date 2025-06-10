from pydantic import BaseModel, Field

class Expense(BaseModel):
    id: int
    description: str
    amount: float = Field(gt=0)
    currency: str | None