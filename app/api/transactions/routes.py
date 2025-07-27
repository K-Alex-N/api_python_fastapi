from typing import List
from uuid import UUID

from fastapi import APIRouter, HTTPException

from ..categories.models import Category
from .schemas import TransactionCreate, TransactionOut, TransactionUpdate
from .models import Transaction

router = APIRouter(prefix="/transactions", tags=["Transactions"])


@router.get("/", response_model=List[TransactionOut])
async def get_transactions() -> List[TransactionOut]:
    txs = await Transaction.find_all(fetch_links=True).to_list()
    return TransactionOut.from_model_list(txs)


@router.post("/", response_model=TransactionOut)
async def create_transaction(data: TransactionCreate) -> TransactionOut:
    category = await Category.get(data.category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    tx = Transaction(
        **data.model_dump(exclude={"category_id"}),
        category=category  # type: ignore
    )
    await tx.insert()  # type: ignore
    return TransactionOut.from_model(tx)


@router.get("/{transaction_id}", response_model=TransactionOut)
async def get_transaction(transaction_id: UUID) -> TransactionOut:
    tx = await Transaction.get(transaction_id, fetch_links=True)
    if not tx:
        raise HTTPException(status_code=404, detail="Transaction not found")

    return TransactionOut.from_model(tx)


@router.patch("/{transaction_id}", response_model=TransactionOut)
async def update_transaction(transaction_id: UUID, data: TransactionUpdate) -> TransactionOut:
    tx = await Transaction.get(transaction_id, fetch_links=True)
    if not tx:
        raise HTTPException(status_code=404, detail="Transaction not found")

    update_data = data.model_dump(exclude_unset=True)

    if "category_id" in update_data:
        new_category = await Category.get(update_data["category_id"])
        if not new_category:
            raise HTTPException(status_code=404, detail="New category not found")
        tx.category = new_category  # type: ignore
        update_data.pop("category_id")

    for field, value in update_data.items():
        setattr(tx, field, value)

    await tx.save()  # type: ignore
    return TransactionOut.from_model(tx)


@router.delete("/{transaction_id}", response_model=dict)
async def delete_transaction(transaction_id: UUID) -> dict:
    tx = await Transaction.get(transaction_id)
    if not tx:
        raise HTTPException(status_code=404, detail="Transaction not found")

    await tx.delete()  # type: ignore
    return {"message": "Transaction deleted successfully"}
