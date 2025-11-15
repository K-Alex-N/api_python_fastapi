from datetime import datetime
from uuid import UUID

from pydantic import RootModel, Field

from ..categories.schemas import CategoryOut
from ..schemas import BaseOutModel


class TransactionBase(BaseOutModel):
    amount: float = Field(ge=0, description="Amount must be greater than or equal to 0")
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
    amount: float | None = Field(None, ge=0, description="Amount must be greater than or equal to 0")
    date: datetime | None = None
    description: str | None = None
    category_id: UUID | None = None
