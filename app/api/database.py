import os

from contextlib import asynccontextmanager

from beanie import init_beanie
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

from .categories.models import Category
from .transactions.models import Transaction

MONGO_HOST = os.getenv("MONGO_HOST", "localhost")
MONGO_URL = f"mongodb://{MONGO_HOST}:27017"

async_client = AsyncIOMotorClient(MONGO_URL)
async_db = async_client["async_db"]


@asynccontextmanager
async def lifespan(app: FastAPI):
    client = AsyncIOMotorClient(
        MONGO_URL,
        uuidRepresentation="standard"
    )
    db = client.my_finance
    await init_beanie(database=db, document_models=[Transaction, Category])
    yield
    client.close()
