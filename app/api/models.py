# from pydantic import BaseModel, Field
# from typing import List
#
#
# class Expense(BaseModel):
#     id: int
#     description: str
#     amount: float = Field(gt=0)
#     currency: str | None
#
#
# class Expenses(BaseModel):
#     expenses: List[Expense]


def transaction_helper(transaction: dict) -> dict:
    return {
        "id": str(transaction["_id"]),
        "amount": transaction["amount"],
        "category": transaction["category"],
        "type": transaction["type"],
        "description": transaction.get("description"),
        "timestamp": transaction["timestamp"],
    }
