import allure
import requests
import time
import os

from app.api.models import Expense

from .common.common import clean_up_db

BASE_URL = os.getenv("BASE_URL", "http://localhost:8000")  # для докера возьмет http://api:8000 из композ-ямл

@allure.epic("API")
class TestAPI:
    def test_get_expenses(self):
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

    # def test_create_user(authenticated_api_client):
    #     new_user_data = generate_random_user_data()
    #     response = authenticated_api_client.create_user(new_user_data)
    #     assert response.status_code == 201 # Created
    #     created_user = response.json()
    #     assert created_user["email"] == new_user_data["email"]
    #     assert "id" in created_user
    #
    #     # Можно проверить, что пользователь действительно создан
    #     get_response = authenticated_api_client.get_user(created_user["id"])
    #     assert get_response.status_code == 200
    #     assert get_response.json()["email"] == new_user_data["email"]

    # class test_add_expense

    # def test_add_expense():  # он же должен какой то файл получить или что????
    #     create_one_expense()
    #     expenses = get_expenses()

    # def test_get_expense_with_valid_id():
    #     create_one_expense()
    #     response = requests.get(BASE_URL + "/1")
    #     assert response.status_code == 200
    #     clean_up_db()  # это все лучше вынести в фикстуры

    def test_get_expense_with_invalid_id(self):
        response = requests.get(BASE_URL + "/123")
        assert response.status_code == 404  # под номером 123 ничего нет, в базе вообще ничего нет
        clean_up_db()  # это все лучше вынести в фикстуры


expense1 = Expense(
    id=1,
    description="Мороженка",
    amount=100,
    currency="RSD",
)

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
