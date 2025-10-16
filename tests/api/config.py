import os

APP_HOST = os.getenv("APP_HOST", "localhost")
BASE_URL = f"http://{APP_HOST}:8000"
