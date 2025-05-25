import uvicorn
from fastapi import FastAPI

from tests.test_fastapi import spending1

app = FastAPI()

spendings = [
    ["мороженка", "100", "Дин"],
    ["Аренда квартиры", "330", "Евро"],
    ["Годовая подписка Яндекс", "2990", "Руб"]
]


@app.get("/balance")
def get_balance():



# def add_expense():
# Date
# Amount
# Description
# currency

# def add_income():
# Delete

# def modify_expense():

# Recurring Expense
# One-time Expense
# аренда квартиры


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
