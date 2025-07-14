from datetime import datetime
from uuid import UUID, uuid4
from enum import Enum

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
    type: str  # 'income' or 'expense'

    class Settings:
        name = "categories"