from uuid import UUID
from typing import Optional, Literal

from app.api.schemas import BaseOutModel


class CategoryBase(BaseOutModel):
    name: str
    type: Literal["income", "expense"]


class CategoryCreate(CategoryBase):
    pass


class CategoryOut(CategoryBase):
    id: UUID


class CategoryUpdate(BaseOutModel):
    name: Optional[str] = None
    type: Optional[Literal["income", "expense"]] = None
