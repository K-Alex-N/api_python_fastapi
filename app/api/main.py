import random

import uvicorn

# from fastapi import FastAPI, HTTPException
#
# from .models import Expense
#
# app = FastAPI()
#
# expenses = []
#
# @app.get("/")
# def get_expenses():
#     return expenses
#
#
# @app.get("/expenses_amount")
# def get_expenses_amount():
#     return sum(expense["amount"] for expense in expenses)
#
#
# @app.get("/{id}")
# def get_expense(id: int):
#     for s in expenses:
#         if s["id"] == id:
#             return s
#     raise HTTPException(status_code=404, detail="Not found")
#
#
# @app.post("/")
# def add_expense(expense: Expense):
#     expenses.append({
#         "id": len(expenses) + 1,
#         "description": expense.description,
#         "amount": expense.amount,
#         "currency": expense.currency
#     })
#     return {"success": True, "message": "Expense added"}
#
#
# @app.put("/{id}")
# def update_expense(id: int, expense: Expense):
#     ...
#
#
# @app.delete("/{id}")
# def delete_expense(id: int):
#     ...

# ---------------------------------------------------------

# from fastapi import FastAPI, HTTPException
#
# from .schemas import TransactionCreate, Transaction
# from .crud import add_transaction, get_all_transactions, delete_transaction
#
# app = FastAPI()
#
# @app.post("/transactions", response_model=Transaction)
# async def create_transaction(transaction: TransactionCreate):
#     return await add_transaction(transaction)
#
# @app.get("/transactions", response_model=list[Transaction])
# async def read_transactions():
#     return await get_all_transactions()
#
# @app.delete("/transactions/{transaction_id}")
# async def remove_transaction(transaction_id: str):
#     deleted = await delete_transaction(transaction_id)
#     if not deleted:
#         raise HTTPException(status_code=404, detail="Transaction not found")
#     return {"message": "Deleted successfully"}


# ---------------------------------------------------------

# from fastapi import FastAPI, HTTPException
# from schemas import Transaction, TransactionCreate
# from crud_async import add_transaction_async, delete_transaction_async
# from crud_sync import get_all_transactions_sync
#
# app = FastAPI(title="Finance Tracker with Sync + Async")
#
# @app.post("/transactions", response_model=Transaction)
# async def create_transaction(transaction: TransactionCreate):
#     return await add_transaction_async(transaction)
#
# @app.get("/transactions", response_model=list[Transaction])
# def get_transactions():
#     return get_all_transactions_sync()
#
# @app.delete("/transactions/{transaction_id}")
# async def delete_transaction(transaction_id: str):
#     deleted = await delete_transaction_async(transaction_id)
#     if not deleted:
#         raise HTTPException(status_code=404, detail="Transaction not found")
#     return {"message": "Deleted successfully"}

# ---------------------------------------------------------

from fastapi import FastAPI, HTTPException, Request, Response
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Counter, Gauge
import string

from app.api.database import lifespan
from app.api.logger_config import setup_logger
# from .logger_config import setup_logger
# from .schemas import Transaction, HealthCheckResponse
# from .crud_async import add_random_transaction_async, get_random_transaction_async
# from .crud_sync import add_random_transaction_sync, get_random_transaction_sync

logger = setup_logger()
app = FastAPI(lifespan=lifespan)

from app.api.transactions import routes as transactions_routes
from app.api.categories import routes as categories_routes

# app.include_router(routes.router)
app.include_router(transactions_routes.router)
app.include_router(categories_routes.router)







# --- Healthcheck ---


# from .database import async_db, sync_db
# from pymongo.errors import PyMongoError
# from motor.core import AgnosticDatabase
# from fastapi.responses import JSONResponse
#
#
# @app.get("/health")
# async def healthcheck():
#     await async_db.command("ping")
#     return {"status": "ok"}
#
#
# @app.post("/test_add")
# async def test_post():
#     await async_db.transactions.insert_one({"amount": 14})
#
#
# # --- ASYNC Routes ---
#
# @app.post("/async/transaction", response_model=Transaction)
# async def create_async_transaction():
#     return await add_random_transaction_async()
#
#
# @app.get("/async/transaction", response_model=Transaction)
# async def read_async_transaction():
#     transaction = await get_random_transaction_async()
#     if not transaction:
#         raise HTTPException(status_code=404, detail="No transactions found")
#     return transaction
#
#
# # --- SYNC Routes ---
#
# @app.post("/sync/transaction", response_model=Transaction)
# def create_sync_transaction():
#     return add_random_transaction_sync()
#
#
# @app.get("/sync/transaction", response_model=Transaction)
# def read_sync_transaction():
#     transaction = get_random_transaction_sync()
#     if not transaction:
#         raise HTTPException(status_code=404, detail="No transactions found")
#     return transaction

# ---------------for elastic------------------------------------------
#
# @app.middleware("http")
# async def log_requests(request: Request, call_next):
#     ip = request.client.host
#     endpoint = request.url.path
#     method = request.method
#
#     response: Response = await call_next(request)
#     status_code = response.status_code
#
#     logger.info(
#         f"{method} {endpoint} - {status_code}",
#         extra={
#             "extra": {
#                 "ip": ip,
#                 "endpoint": endpoint,
#                 "method": method,
#                 "status": status_code,
#             }
#         }
#     )
#
#     return response
#
#
#
# @app.get("/generate-random-logs")
# def generate_random_logs():
#     levels = ["info", "debug", "warning", "error", "supper_error"]
#     actions = ["login", "logout", "purchase", "view", "click"]
#     countries = ["US", "DE", "FR", "IN", "RU", "CN", "BR"]
#     devices = ["mobile", "desktop", "tablet", "smart_tv"]
#
#     for _ in range(10):
#         level = random.choice(levels)
#         log_data = {
#             "user_id": random.randint(1000, 9999),
#             "action": random.choice(actions),
#             "duration": round(random.uniform(0.1, 5.0), 2),
#             "success": random.choice([True, False]),
#             "country": random.choice(countries),
#             "device": random.choice(devices),
#             "session_id": ''.join(random.choices(string.ascii_letters + string.digits, k=12))
#         }
#
#         msg = f"User {log_data['user_id']} performed {log_data['action']}"
#
#         # Логируем на нужном уровне
#         getattr(logger, level)(
#             msg,
#             extra={"extra": log_data}
#         )
#
#     return {"message": "Random logs generated"}
#
# # ---------------for prometheus------------------------------------------
#
# Instrumentator().instrument(app).expose(app)
#
# ERROR_COUNTER = Counter("fastapi_errors_total", "Total number of simulated errors")
# ACTIVE_USERS = Gauge("fastapi_active_users", "Number of active users")
#
# @app.get("/")
# def read_root():
#     ACTIVE_USERS.set(random.randint(5, 50))  # Пример бизнес-метрики
#     return {"message": "Hello from FastAPI"}
#
# @app.get("/error")
# def generate_error():
#     ERROR_COUNTER.inc()
#     raise ValueError("Simulated error")

# ---------------------------------------------------------

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

# improvements
# date (auto + modification)
# Expense One-time + Recurring
# add_income
