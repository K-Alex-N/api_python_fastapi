from uuid import UUID, uuid4

from typing import Literal
from pydantic import Field
from beanie import Document


class Category(Document):
    id: UUID = Field(default_factory=uuid4)
    name: str
    type: Literal["income", "expense"]

    class Settings:
        name = "categories"
