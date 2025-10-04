from typing import List, Literal, Optional
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


class CategoryOutList(RootModel[List[CategoryOut]]):
    pass


class CategoryUpdate(BaseOutModel):
    name: Optional[str] = None
    type: Optional[Literal["income", "expense"]] = None
