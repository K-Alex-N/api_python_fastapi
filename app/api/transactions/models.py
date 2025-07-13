from datetime import datetime
from uuid import UUID
from enum import Enum

from pydantic import Field
from beanie import Document







class Transaction(Document):
    amount: float = Field(gt=0)
    category_id: UUID | None = None
    date: datetime = Field(default_factory=datetime.now)
    description: str | None = Field(None, max_length=1000)

    class Settings:
        name = "transactions"


class Category(Document):
    id: UUID
    name: str
    type: str  # create Type - не нужно уже проверено пайдентиком
