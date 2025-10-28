from contextlib import asynccontextmanager

from beanie import init_beanie
from fastapi import FastAPI, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient

from .categories.models import Category
from .config import MONGO_URL
from .transactions.models import Transaction

async_client = AsyncIOMotorClient(MONGO_URL)  # попробовать закаментить эти две строчки
async_db = async_client["async_db"]  #


client = None
database = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    global client, database
    try:
        client = AsyncIOMotorClient(MONGO_URL, uuidRepresentation="standard")
        # database = client.my_finance
        database = client.get_database()
        await init_beanie(database=database, document_models=[Transaction, Category])
        yield
    finally:
        if client:
            client.close()


# --- Функция получения БД для Dependency Injection ---
def get_database():
    """
    Возвращает экземпляр базы данных.
    Это ключевая функция, которую мы будем подменять в тестах.
    """
    global database
    if database is None:
        # В реальном приложении это должно быть невозможно после запуска lifespan
        raise HTTPException(status_code=503, detail="Database not initialized")
    return database
