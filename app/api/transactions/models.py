from datetime import datetime
from uuid import UUID, uuid4

from pydantic import Field
from beanie import Document, Link

from app.api.categories.models import Category


# class Transaction(Document):
#     # id: str | UUID = Field(default_factory=uuid4, alias="_id")
#     # id: str
#     amount: float = Field(gt=0)
#     category_id: str | UUID | None = None
#     date: datetime = Field(default_factory=datetime.now)
#     description: str | None = Field(None, max_length=1000)
#
#     class Settings:
#         name = "transactions"

class Transaction(Document):
    id: UUID = Field(default_factory=uuid4)
    amount: float = Field(gt=0)
    date: datetime
    description: str = ""
    category: Link[Category]

    # category: Link[Category] | Category

    class Settings:
        name = "transactions"
