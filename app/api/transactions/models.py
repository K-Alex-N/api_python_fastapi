from datetime import datetime
from uuid import UUID, uuid4

from beanie import Document, Link
from pydantic import Field

from ..categories.models import Category


class Transaction(Document):
    id: UUID = Field(default_factory=uuid4)
    amount: float = Field(ge=0)
    date: datetime
    description: str = ""
    category: Link[Category]

    class Settings:
        name = "transactions"
