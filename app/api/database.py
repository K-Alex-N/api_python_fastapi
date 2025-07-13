# import os
#
# from motor.motor_asyncio import AsyncIOMotorClient
# from pymongo import MongoClient
#
#
# MONGO_HOST = os.getenv("MONGO_HOST", "localhost")
# MONGO_URL = f"mongodb://{MONGO_HOST}:27017"
#
# async_client = AsyncIOMotorClient(MONGO_URL)
# async_db = async_client["async_db"]
#
# sync_client = MongoClient(MONGO_URL)
# sync_db = sync_client["sync_db"]

#beanie
from contextlib import asynccontextmanager

from beanie import init_beanie
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

from app.api.transactions.models import Transaction

# from models import Transaction, Category

MONGO_URI = "mongodb://localhost:27017"


@asynccontextmanager
async def lifespan(app: FastAPI):
    client = AsyncIOMotorClient(MONGO_URI)
    db = client.test
    # await init_beanie(database=db, document_models=[Transaction, Category])
    await init_beanie(database=db, document_models=[Transaction])
    yield
    client.close()


