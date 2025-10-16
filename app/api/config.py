import os

MONGO_HOST = os.getenv("MONGO_HOST", "localhost")
MONGO_URL = f"mongodb://{MONGO_HOST}:27017"
