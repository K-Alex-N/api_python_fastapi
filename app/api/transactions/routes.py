from typing import List

from fastapi import APIRouter, HTTPException

from app.api.categories.models import Category
from app.api.transactions.schemas import TransactionCreate, TransactionOut
from app.api.transactions.models import Transaction

router = APIRouter(prefix="/transactions", tags=["Transactions"])


@router.get("/", response_model=List[TransactionOut])
async def get_transactions() -> List[TransactionOut]:
    txs = await Transaction.find_all(fetch_links=True).to_list()
    return TransactionOut.from_model_list(txs)


@router.get("/{id}", response_model=TransactionOut)
async def get_transaction_by_id(transaction_id: int) -> TransactionOut:
    tx = await Transaction.find_by_id(transaction_id)
    if not tx:
        raise HTTPException(status_code=404, detail="Transaction not found")

    return TransactionOut.from_model(tx)


# @router.get("/{id}")
# async def get_transaction(id: int) -> TransactionOut: # скорее Object_id или UUID должен быть
#     tx = await Transaction.find_by_id(id)
#     if not tx:
#         raise HTTPException(status_code=404, detail="Transaction not found")
#     return tx


# # @router.post("/")
# @router.post("/", response_model=TransactionOut)
# async def create_transaction(transaction: TransactionCreate):
# # async def create_transaction(transaction: TransactionCreate) -> TransactionOut:
#     tx = Transaction(**transaction.model_dump())
#     await tx.insert()
#     return tx
#     # return TransactionOut.from_model(tx)

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
