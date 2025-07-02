import random
from faker import Faker
from datetime import datetime

from .database import async_db
from .models import transaction_helper

faker = Faker()
collection = async_db.transactions


async def add_random_transaction_async():
    data = {
        "amount": round(random.uniform(10, 2000)),
        "category": random.choice(["food", "transport", "shopping", "salary"]),
        "type": random.choice(["income", "expense"]),
        "description": faker.sentence(),
        "timestamp": datetime.now()
    }
    result = await collection.insert_one(data)
    doc = await collection.find_one({"_id": result.inserted_id})
    return transaction_helper(doc)


async def get_random_transaction_async():
    count = await collection.count_documents({})
    if count == 0:
        return None
    skip = random.randint(0, count - 1)
    cursor = collection.find().skip(skip).limit(1)
    doc = await cursor.to_list(length=1)
    return transaction_helper(doc[0])
