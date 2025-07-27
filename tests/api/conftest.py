import pytest
# from pymongo import MongoClient
#
# from app.api.database import MONGO_URL
from tests.api.services.categories.create_category import CreateCategory
from tests.api.services.categories.payloads import payloads
from tests.api.services.transactions.payloads import payloads as payload_trnx
from tests.api.services.transactions.create_transaction import CreateTransaction


# @pytest.fixture(scope="session", autouse=True)
# def drop_db():
#     client = MongoClient(MONGO_URL)
#     client.drop_database("my_finance")
#     client.close()

def clean_db():
    pass

@pytest.fixture(scope="session", autouse=True)
def prefill_db():
    number_of_categories = 2
    for _ in range(number_of_categories):
        CreateCategory().create_category(payloads.category())

    number_of_transactions = 2
    for _ in range(number_of_transactions):
        CreateTransaction().create_transaction(payload_trnx.create_transaction())
