from typing import Literal
from uuid import UUID

from pydantic import RootModel

from ..schemas import BaseOutModel


class CategoryBase(BaseOutModel):
    name: str
    type: Literal["income", "expense"]


class CategoryCreate(CategoryBase):
    pass


class CategoryOut(CategoryBase):
    id: UUID


class CategoryOutList(RootModel[list[CategoryOut]]):
    pass


class CategoryUpdate(BaseOutModel):
    name: str | None = None
    type: Literal["income", "expense"] | None = None
