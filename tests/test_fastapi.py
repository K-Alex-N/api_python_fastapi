import requests
import time

# BASE_URL = "http://localhost:8000/"
# BASE_URL = "http://host.docker.internal:8000/"
import os
# BASE_URL = os.getenv("BASE_URL", "http://localhost:8000")
BASE_URL = "http://api:8000"


# Очень редко тесты успевают запуститься до того как сервак ФастАПИ поднимится
#
# for i in range(10):
#     try:
#         response = requests.get(BASE_URL)
#         if response.status_code == 200:
#             break
#     except requests.exceptions.ConnectionError:
#         print("!!!!!!!!!!!!!!!!Ждём, пока API поднимется...")
#         time.sleep(1)
# else:
#     raise RuntimeError("API не поднялся вовремя")

def test_get():
    response = requests.get(BASE_URL)
    assert response.status_code == 200

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
