# import pytest
# from pymongo import MongoClient
#
# from app.api.database import MONGO_URL
# from tests.api.services.categories.create_category import CreateCategory
# from tests.api.services.categories.payloads import payloads
#
#
# @pytest.fixture(scope="session", autouse=True)
# def prefill_db():
#     for _ in range(2):
#         CreateCategory().create_category(payloads.category())
#
#
# @pytest.fixture(scope="session", autouse=True)
# def drop_db():
#     client = MongoClient(MONGO_URL)
#     client.drop_database("my_finance")
#     client.close()
