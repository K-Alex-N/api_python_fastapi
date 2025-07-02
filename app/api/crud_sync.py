from .database import sync_db
from .models import transaction_helper
import random
from faker import Faker
from datetime import datetime

faker = Faker()
collection = sync_db.transactions

def add_random_transaction_sync():
    data = {
        "amount": round(random.uniform(10, 1000), 2),
        "category": random.choice(["food", "transport", "shopping", "salary"]),
        "type": random.choice(["income", "expense"]),
        "description": faker.sentence(),
        "timestamp": datetime.now()
    }
    result = collection.insert_one(data)
    doc = collection.find_one({"_id": result.inserted_id})
    return transaction_helper(doc)

def get_random_transaction_sync():
    count = collection.count_documents({})
    if count == 0:
        return None
    skip = random.randint(0, count - 1)
    doc = collection.find().skip(skip).limit(1)[0]
    return transaction_helper(doc)
