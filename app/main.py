import uvicorn
from fastapi import FastAPI, HTTPException

from app.models import Expense

app = FastAPI()

expenses = {}


@app.get("/")
def get_expenses():
    return expenses


@app.get("/expenses_amount")
def get_expenses_amount():
    return sum(expense["amount"] for expense in expenses)


@app.get("/{id}")
def get_expense(id: int):
    for s in expenses:
        if s["id"] == id:
            return s
    raise HTTPException(status_code=404, detail="Not found")


@app.post("/")
def add_expense(expense: Expense):
    expenses.append({
        "id": len(expenses) + 1,
        "description": expense.description,
        "amount": expense.amount,
        "currency": expense.currency
    })
    return {"success": True, "message": "Expense added"}


@app.put("/{id}")
def update_expense(id: int, expense: Expense):
    ...


@app.delete("/{id}")
def delete_expense(id: int):
    ...


if __name__ == "__main__":  # это не запускается если через Докер!!!
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

# improvements
# date (auto + modification)
# Expense One-time + Recurring
# add_income
