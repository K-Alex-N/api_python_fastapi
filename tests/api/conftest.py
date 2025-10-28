
import pytest
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from app.api.categories.models import Category
from app.api.config import MONGO_URL
from app.api.transactions.models import Transaction
from tests.api.services.categories.create_category import CreateCategory
from tests.api.services.categories.payloads import payloads
from tests.api.services.transactions.create_transaction import CreateTransaction
from tests.api.services.transactions.payloads import payloads as payload_trnx


@pytest.fixture(scope="session", autouse=True)
def anyio_backend():
    return "asyncio"


@pytest.fixture(scope="session", autouse=True)
async def initialize_db():
    client = AsyncIOMotorClient(MONGO_URL, uuidRepresentation="standard")
    db = client.my_finance  # DB name from app/api/database.py
    await init_beanie(database=db, document_models=[Transaction, Category])


# Existing prefill_db fixture below
@pytest.fixture(scope="session", autouse=True)
def prefill_db() -> None:
    number_of_categories = 3
    for _ in range(number_of_categories):
        CreateCategory().create_category(payloads.category())

    number_of_transactions = 3
    for _ in range(number_of_transactions):
        CreateTransaction().create_transaction(payload_trnx.create_transaction())
