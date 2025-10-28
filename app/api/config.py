import os

MONGO_HOST = os.getenv("MONGO_HOST", "localhost")
DB_NAME = "my_finance"
MONGO_URL = f"mongodb://{MONGO_HOST}:27017/{DB_NAME}"
