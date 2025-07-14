from datetime import datetime
from enum import Enum
from uuid import UUID

from bson import ObjectId
from pydantic import BaseModel, Field


# class Type(Enum):
#     INCOME = "income"
#     EXPENSE = "expense"
#
#
# class CategoryCreate(BaseModel):
#     name: str
#     type: str  # 'income' or 'expense'
#
#
# class CategoryOut(CategoryCreate):
#     # id: ObjectId
#     id: str | UUID

class CategoryCreate(BaseModel):
    name: str
    type: str  # 'income' or 'expense'

class CategoryOut(BaseModel):
    id: UUID
    name: str
    type: str


# class Categories:
#     id: int
#     type: Type
#
#
# asd = Categories()
# asd.type = Type.INCOME