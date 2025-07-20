import os

from app.api.categories.models import Category
from app.api.transactions.models import Transaction

from contextlib import asynccontextmanager

from beanie import init_beanie
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_HOST = os.getenv("MONGO_HOST", "localhost")
MONGO_URL = f"mongodb://{MONGO_HOST}:27017"

# async_client = AsyncIOMotorClient(MONGO_URL)
# async_db = async_client["async_db"]
#
# sync_client = MongoClient(MONGO_URL)
# sync_db = sync_client["sync_db"]

@asynccontextmanager
async def lifespan(app: FastAPI):
    client = AsyncIOMotorClient(
        MONGO_URL,
        uuidRepresentation="standard"
    )
    db = client.test
    await init_beanie(database=db, document_models=[Transaction, Category])
    yield
    client.close()
