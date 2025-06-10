import requests
import time

import os

from tests.api.common import *

BASE_URL = os.getenv("BASE_URL", "http://localhost:8000")  # для докера возьмет http://api:8000 из композ-ямл

# для Докер-композ. Часто тесты успевают пройти до того как сервак ФастАПИ поднимится
for i in range(3):
    try:
        response = requests.get(BASE_URL)
        if response.status_code == 200:
            break
    except requests.exceptions.ConnectionError:
        print("!!!!!!!!!!!!!!!!Ждём, пока сервак поднимется...")
        time.sleep(1)
else:
    raise RuntimeError("API так и не поднялся")


# class test_get_expenses:
#     URL = BASE_URL
def test_get_expenses():
    # response = requests.get(URL)
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    assert response.reason == "OK"

    # try:
    #     response = requests.get(BASE_URL)
    #
    #     if response.status_code == 200:
    #         data = response.json()
    #         print(data)
    #     else:
    #         print(f"Ошибка при выполнении запроса. Код статуса: {response.status_code}")
    #         print(f"Текст ошибки: {response.text}")
    #
    # except requests.exceptions.RequestException as e:
    #     print(f"Произошла ошибка при подключении к API: {e}")


# class test_add_expense


def test_add_expense():  # он же должен какой то файл получить или что????
    create_one_expense()
    expenses = get_expenses()


def test_get_expense_with_valid_id(id: int):
    create_one_expense()
    response = requests.get(BASE_URL + "/" + str(id))
    assert response.status_code == 200
    clean_up_db()  # это все лучше вынести в фикстуры


def test_get_expense_with_invalid_id():
    response = requests.get(BASE_URL + "/123")
    assert response.status_code == 404  # под номером 123 ничего нет, в базе вообще ничего нет
    clean_up_db()  # это все лучше вынести в фикстуры


expense1 = {
    "id": 1,
    "description": "Мороженка",
    "amount": 100,
}
expense2 = {
    "id": 2,
    "description": "Хлебушек",
    "amount": 95,
}

expense3 = {
    "id": 3,
    "description": "Лимонадик",
    "amount": 69,
}

expenses = [
    {
        "id": 1,
        "description": "Мороженка111111",
        "amount": 100,
    },
    {
        "id": 2,
        "description": "Хлебушек222",
        "amount": 95,
    },
    {
        "id": 3,
        "description": "Лимонадик",
        "amount": 69,
    }
]
