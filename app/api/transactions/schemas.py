from datetime import datetime
from uuid import UUID

from pydantic import RootModel

from ..categories.schemas import CategoryOut
from ..schemas import BaseOutModel


class TransactionBase(BaseOutModel):
    amount: float
    date: datetime
    description: str


class TransactionCreate(TransactionBase):
    category_id: UUID


class TransactionOut(TransactionBase):
    id: UUID
    category: CategoryOut


class TransactionOutList(RootModel[list[TransactionOut]]):
    pass


class TransactionUpdate(BaseOutModel):
    amount: float | None = None
    date: datetime | None = None
    description: str | None = None
    category_id: UUID | None = None
