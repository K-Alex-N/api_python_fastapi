from contextlib import asynccontextmanager

from beanie import init_beanie
from fastapi import FastAPI, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient

from .categories.models import Category
from .config import MONGO_URL
from .transactions.models import Transaction

async_client = AsyncIOMotorClient(MONGO_URL)
async_db = async_client["async_db"]


client = None
database = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    global client, database
    try:
        client = AsyncIOMotorClient(MONGO_URL, uuidRepresentation="standard")
        database = client.get_database()
        await init_beanie(database=database, document_models=[Transaction, Category])
        yield
    finally:
        if client:
            client.close()


def get_database():
    global database
    if database is None:
        raise HTTPException(status_code=503, detail="Database not initialized")
    return database
