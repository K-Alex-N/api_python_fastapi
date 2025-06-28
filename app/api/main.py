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

from fastapi import FastAPI, HTTPException

from .schemas import TransactionCreate, Transaction
from .crud import add_transaction, get_all_transactions, delete_transaction

app = FastAPI(title="Personal Finance Tracker")

@app.post("/transactions", response_model=Transaction)
async def create_transaction(transaction: TransactionCreate):
    return await add_transaction(transaction)

@app.get("/transactions", response_model=list[Transaction])
async def read_transactions():
    return await get_all_transactions()

@app.delete("/transactions/{transaction_id}")
async def remove_transaction(transaction_id: str):
    deleted = await delete_transaction(transaction_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return {"message": "Deleted successfully"}


# ---------------------------------------------------------



if __name__ == "__main__":  # это не запускается если через Докер!!!
    uvicorn.run("main:app", reload=True)

# improvements
# date (auto + modification)
# Expense One-time + Recurring
# add_income


