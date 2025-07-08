import os

from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient


MONGO_HOST = os.getenv("MONGO_HOST", "localhost")
MONGO_URL = f"mongodb://{MONGO_HOST}:27017"

async_client = AsyncIOMotorClient(MONGO_URL)
async_db = async_client["async_db"]

sync_client = MongoClient(MONGO_URL)
sync_db = sync_client["sync_db"]

