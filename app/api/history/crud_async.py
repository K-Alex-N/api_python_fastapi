from bson import ObjectId
from schemas import TransactionCreate
from database import async_db
from models import transaction_helper

collection = async_db.transactions

async def add_transaction_async(transaction_data: TransactionCreate):
    result = await collection.insert_one(transaction_data.dict())
    new_transaction = await collection.find_one({"_id": result.inserted_id})
    return transaction_helper(new_transaction)

async def delete_transaction_async(id: str):
    result = await collection.delete_one({"_id": ObjectId(id)})
    return result.deleted_count == 1
