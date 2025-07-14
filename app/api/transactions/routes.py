from typing import List

from fastapi import APIRouter, HTTPException

from app.api.categories.models import Category
from app.api.transactions.schemas import TransactionCreate, TransactionOut
from app.api.transactions.models import Transaction

router = APIRouter(prefix="/transactions", tags=["Transactions"])

@router.get("/", response_model=List[TransactionOut])
# @router.get("/")
# async def get_transactions():
async def get_transactions() -> List[TransactionOut]:
    txs = await Transaction.find_all(fetch_links=True).to_list()
    # return txs
    return [TransactionOut.from_model(tx) for tx in txs]

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

    # tx = Transaction(
    #     amount=data.amount,
    #     date=data.date,
    #     description=data.description,
    #     category=category
    # )
    # await tx.insert()
    # return TransactionOut.from_model(tx)


    tx = Transaction(
        **data.model_dump(exclude={"category_id"}),
        category=category # type: ignore
    )
    await tx.insert()
    return TransactionOut.from_model(tx)



# @router.post("/")
# async def create_transaction(data: TransactionCreate):
#     category = await Category.get(data.category_id)
#     if not category:
#         raise HTTPException(status_code=404, detail="Category not found")
#     tx = Transaction(**data.dict(exclude={"category_id"}), category=category)
#     await tx.insert()
#     return tx





# @router.get("/users/", tags=["users"])
# async def read_users():
#     return [{"username": "Rick"}, {"username": "Morty"}]
#
#
# @router.get("/users/me", tags=["users"])
# async def read_user_me():
#     return {"username": "fakecurrentuser"}
#
#
# @router.get("/users/{username}", tags=["users"])
# async def read_user(username: str):
#     return {"username": username}