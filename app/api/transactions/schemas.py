from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import RootModel

from app.api.categories.schemas import CategoryOut
from app.api.schemas import BaseOutModel


class TransactionBase(BaseOutModel):
    amount: float
    date: datetime
    description: str


class TransactionCreate(TransactionBase):
    category_id: UUID


class TransactionOut(TransactionBase):
    id: UUID
    category: CategoryOut


class TransactionOutList(RootModel[List[TransactionOut]]):
    pass


class TransactionUpdate(BaseOutModel):
    amount: Optional[float] = None
    date: Optional[datetime] = None
    description: Optional[str] = None
    category_id: Optional[UUID] = None
