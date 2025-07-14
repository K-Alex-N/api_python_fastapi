from typing import List

from fastapi import APIRouter, HTTPException

from app.api.categories.models import Category
from app.api.categories.schemas import CategoryCreate
from app.api.transactions.schemas import TransactionCreate, TransactionOut
from app.api.transactions.models import Transaction

router = APIRouter(prefix="/categories", tags=["Сategories"])


# @router.get("/")
# async def get_categories() -> List[TransactionOut]:
#     txns = await Transaction.find_all().to_list()
#     return txns
#
#
# @router.get("/{id}")
# async def get_category(id: int) -> TransactionOut:  # скорее Object_id или UUID должен быть
#     txn = await Transaction.find_by_id(id)
#     if not txn:
#         raise HTTPException(status_code=404, detail="Transaction not found")
#     return txn


@router.post("/")
async def create_category(category: CategoryCreate):
    cat = Category(**category.model_dump())
    await cat.insert()
    return cat

# @router.post("/")
# async def create_category(transaction: TransactionCreate) -> TransactionOut:
#     db_txn = Transaction(**transaction.model_dump())
#     await db_txn.insert()
#     return db_txn

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
