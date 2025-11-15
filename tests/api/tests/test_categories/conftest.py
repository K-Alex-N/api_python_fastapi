import pytest_asyncio
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from app.api.categories.models import Category
from app.api.config import DB_NAME


@pytest_asyncio.fixture(scope="session", autouse=True)
async def init_db():
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    db = client[DB_NAME]
    await init_beanie(database=db, document_models=[Category])
    yield
    client.close()
