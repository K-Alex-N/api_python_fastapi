from typing import Literal
from uuid import UUID, uuid4

from beanie import Document
from pydantic import Field


class Category(Document):
    id: UUID = Field(default_factory=uuid4)
    name: str
    type: Literal["income", "expense"]

    class Settings:
        name = "categories"
