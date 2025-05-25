import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

spending = [
    {
        "id": 1,
        "description": "мороженка",
        "amount": 100,
        "currency": "Дин"
    },
    {
        "id": 2,
        "description": "Аренда квартиры",
        "amount": 330,
        "currency": "Евро"
    },
    {
        "id": 3,
        "description": "Годовая подписка Яндекс",
        "amount": 2990,
        "currency": "Руб"
    }
]


@app.get("/balance")
def get_balance():
    return spending


@app.get("/{id}")
def get_spending(id: int):
    for s in spending:
        if s["id"] == id:
            return s
    raise HTTPException(status_code=404, detail="Not found")


class Expense(BaseModel):
    description: str
    amount: int
    currency: str


@app.post("/")
def add_expense(expense: Expense):
    spending.append({
        "id": len(spending) + 1,
        "description": expense.description,
        "amount": expense.amount,
        "currency": expense.currency
    })
    return {"success": True, "message": "Expense added"}


# def add_income():
# Delete

# def modify_expense():

# improvements
# date (auto + modification)
# Expense One-time + Recurring

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
