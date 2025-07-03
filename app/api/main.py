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

from fastapi import FastAPI, HTTPException
from .schemas import Transaction, HealthCheckResponse
from .crud_async import add_random_transaction_async, get_random_transaction_async
from .crud_sync import add_random_transaction_sync, get_random_transaction_sync

app = FastAPI()

# --- Healthcheck ---

# @app.get("/")
# def healthcheck():
#     return {"status": "ok"}

from .database import async_db
from pymongo.errors import PyMongoError
from motor.core import AgnosticDatabase
from fastapi.responses import JSONResponse


# ... другие эндпоинты

# @app.get("/health", summary="Healthcheck")
# @app.get("/health", response_model=HealthCheckResponse)
@app.get("/health")
async def healthcheck():
    return JSONResponse({"status": "ok"})
    # try:
    #     # Быстрая проверка на подключение
    #     await async_db.command("ping")
    #     return {"status": "ok", "database": "up"}
    # except PyMongoError as e:
    #     return JSONResponse(
    #         status_code=503,
    #         content={"status": "error", "database": "down", "details": str(e)}
    #     )


# --- ASYNC Routes ---

@app.post("/async/transaction", response_model=Transaction)
async def create_async_transaction():
    return await add_random_transaction_async()

@app.get("/async/transaction", response_model=Transaction)
async def read_async_transaction():
    transaction = await get_random_transaction_async()
    if not transaction:
        raise HTTPException(status_code=404, detail="No transactions found")
    return transaction

# --- SYNC Routes ---

@app.post("/sync/transaction", response_model=Transaction)
def create_sync_transaction():
    return add_random_transaction_sync()

@app.get("/sync/transaction", response_model=Transaction)
def read_sync_transaction():
    transaction = get_random_transaction_sync()
    if not transaction:
        raise HTTPException(status_code=404, detail="No transactions found")
    return transaction


# ---------------------------------------------------------

if __name__ == "__main__":  # это не запускается если через Докер!!!
    uvicorn.run("main:app", reload=True)

# improvements
# date (auto + modification)
# Expense One-time + Recurring
# add_income


