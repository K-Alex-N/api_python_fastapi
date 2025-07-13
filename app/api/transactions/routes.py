from fastapi import APIRouter

from app.api.transactions.schemas import TransactionCreate
from app.api.transactions.models import Transaction

router = APIRouter()

@router.get("/transactions")
async def get_transactions():
    pass

@router.post("/transactions")
async def create_transaction(transaction: TransactionCreate):
    db_transaction = Transaction(**transaction.model_dump())
    await db_transaction.insert()
    return db_transaction






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