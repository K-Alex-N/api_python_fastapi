# from pydantic import BaseModel, Field
# from typing import Optional
# from datetime import datetime
#
# class TransactionBase(BaseModel):
#     amount: float
#     category: str
#     type: str  # "income" or "expense"
#     description: Optional[str] = None
#     timestamp: datetime = Field(default_factory=datetime.now)
#
# # class TransactionCreate(TransactionBase):
# #     pass
#
# class Transaction(TransactionBase):
#     id: str
#
# class HealthCheckResponse(BaseModel):
#     status: str
#     database: str