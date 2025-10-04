import os
from contextlib import asynccontextmanager

from beanie import init_beanie
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

from .categories.models import Category
from .config import MONGO_URL
from .transactions.models import Transaction

async_client = AsyncIOMotorClient(MONGO_URL)  # попробовать закаментить эти две строчки
async_db = async_client["async_db"]  #


@asynccontextmanager
async def lifespan(app: FastAPI):
    client = AsyncIOMotorClient(MONGO_URL, uuidRepresentation="standard")
    db = client.my_finance
    await init_beanie(database=db, document_models=[Transaction, Category])
    yield
    client.close()
