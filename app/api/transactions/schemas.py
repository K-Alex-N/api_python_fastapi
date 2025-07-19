from datetime import datetime
from uuid import UUID

from bson import ObjectId
from pydantic import BaseModel, Field

from app.api.categories.schemas import CategoryOut
from app.api.schemas import BaseOutModel
from app.api.transactions.models import Transaction


# class TransactionModel(BaseModel):
#     amount: float = Field(gt=0)
#     date: datetime = Field(default_factory=datetime.now)
#     description: str | None = Field(None, max_length=1000)
#
# class TransactionCreate(TransactionModel):
#     # category_id: ObjectId | None = None
#     category_id: str | None = None
#
#
# class TransactionOut(TransactionModel):
#     # id: ObjectId
#     id: str
#     category: CategoryOut
#
#
#     @staticmethod
#     def from_model(tx: Transaction) -> "TransactionOut":
#         return TransactionOut(
#             id=tx.id,
#             amount=tx.amount,
#             date=tx.date,
#             description=tx.description,
#             category=CategoryOut(
#                 id=tx.category.id,
#                 name=tx.category.name,
#                 type=tx.category.type
#             ),
#         )

class TransactionCreate(BaseOutModel):
    amount: float
    date: datetime
    description: str
    category_id: UUID


class TransactionOut(BaseOutModel):
    id: UUID
    amount: float
    date: datetime
    description: str
    # category_id: UUID
    category: CategoryOut

    # @staticmethod
    # def from_model(tx: Transaction) -> "TransactionOut":
    #     return TransactionOut(
    #         id=tx.id,
    #         amount=tx.amount,
    #         date=tx.date,
    #         description=tx.description,
    #         category=CategoryOut(
    #             id=tx.category.id,
    #             name=tx.category.name,
    #             type=tx.category.type
    #         )
    #     )
