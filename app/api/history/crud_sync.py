from database import sync_db
from models import transaction_helper

collection = sync_db.transactions

def get_all_transactions_sync():
    transactions = collection.find()
    return [transaction_helper(t) for t in transactions]
