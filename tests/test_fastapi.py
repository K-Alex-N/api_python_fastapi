import pytest
import requests

BASE_URL = "http://localhost:8000"


def test_get():
    try:
        response = requests.get(BASE_URL)

        if response.status_code == 200:
            data = response.json()
            print(data)
        else:
            print(f"Ошибка при выполнении запроса. Код статуса: {response.status_code}")
            print(f"Текст ошибки: {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"Произошла ошибка при подключении к API: {e}")


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
