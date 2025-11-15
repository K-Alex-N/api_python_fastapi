import pytest
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from app.api.categories.models import Category
from app.api.config import MONGO_URL
from app.api.transactions.models import Transaction
from tests.api.base_client import BaseClient
from tests.api.services.categories.create_category import CreateCategory
from tests.api.services.categories.payloads import payloads
from tests.api.services.transactions.create_transaction import CreateTransaction
from tests.api.services.transactions.payloads import Payloads


@pytest.fixture(scope="session", autouse=True)
def anyio_backend():
    return "asyncio"


@pytest.fixture(scope="session", autouse=True)
async def initialize_db():
    client = AsyncIOMotorClient(MONGO_URL, uuidRepresentation="standard")
    db = client.my_finance
    await init_beanie(database=db, document_models=[Transaction, Category])


@pytest.fixture(scope="function")
def client():
    return BaseClient()


@pytest.fixture(scope="session", autouse=True)
async def prefill_db() -> None:
    number_of_categories = 3
    client = BaseClient()
    for _ in range(number_of_categories):
        create_category = CreateCategory(client)
        await create_category.create_category(payloads.category())

    number_of_transactions = 3
    payload_trnx = Payloads(client)
    for _ in range(number_of_transactions):
        create_transaction = CreateTransaction(client)
        await create_transaction.create_transaction(
            await payload_trnx.create_transaction()
        )
