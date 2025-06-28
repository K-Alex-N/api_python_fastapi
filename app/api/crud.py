from bson import ObjectId
from .database import db
from .models import transaction_helper
from .schemas import TransactionCreate

collection = db.transactions

async def add_transaction(transaction_data: TransactionCreate):
    result = await collection.insert_one(transaction_data.dict())
    new_transaction = await collection.find_one({"_id": result.inserted_id})
    return transaction_helper(new_transaction)

async def get_all_transactions():
    transactions = []
    async for t in collection.find():
        transactions.append(transaction_helper(t))
    return transactions

async def delete_transaction(id: str):
    result = await collection.delete_one({"_id": ObjectId(id)})
    return result.deleted_count == 1
