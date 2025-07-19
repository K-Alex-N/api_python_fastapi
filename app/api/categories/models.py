from datetime import datetime
from uuid import UUID, uuid4
from enum import Enum

from typing import Literal
from pydantic import Field
from beanie import Document


# class Category(Document):
#     # id: UUID
#     # id: UUID = Field(default_factory=uuid4 , alias="_id")
#     id: str | UUID = Field(default_factory=uuid4, alias="_id")
#     # id: str
#     name: str
#     type: str  # create Type - не нужно уже проверено пайдентиком
#
#     class Settings:
#         name = "categories"

class Category(Document):
    id: UUID = Field(default_factory=uuid4)
    name: str
    type: Literal["income", "expense"]

    class Settings:
        name = "categories"