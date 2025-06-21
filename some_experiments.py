import json
from datetime import datetime, timezone

# Your JSON data
json_data = """
{"cookies": [{"name": "session-username", "value": "standard_user", "domain": "www.saucedemo.com", "path": "/", "expires": 1750505128, "httpOnly": false, "secure": false, "sameSite": "Lax"}], "origins": [{"origin": "https://www.saucedemo.com", "localStorage": [{"name": "backtrace-guid", "value": "9c4365ee-3069-4ff8-bba0-cf578b5b0ddb"}, {"name": "backtrace-last-active", "value": "1750504528616"}]}]}
"""

def check_cookie_expiration(json_string: str) -> None:
    """
    Парсит JSON, извлекает дату истечения срока действия куки и сравнивает ее с текущей датой.
    """
    data = json.loads(json_string)

    cookies = data["cookies"]
    expires_timestamp = cookies[0]["expires"]

    print(f"cookies: {cookies}")
    print(f"expires_timestamp: {expires_timestamp}")
    print(datetime.now(timezone.utc).isoformat())
    now = datetime.now().timestamp()
    print(now)

    print(expires_timestamp - now)

    # !!!!!!!!!!!!!!!!!!
    # почему-то "expires_timestamp - now" получается отрицательным, те как будто все протухло, но Прога продолжает спокойно заходить на сайт


    # if not cookies:
    #     print("В JSON-данных не найдено куки.")
    #     return
    #
    # for cookie in cookies:
    #     cookie_name = cookie.get("name", "Неизвестное имя куки")
    #     expires_timestamp = cookie.get("expires")
    #
    #     if expires_timestamp is None:
    #         print(f"Для куки '{cookie_name}' не найдена дата истечения срока действия ('expires').")
    #         continue
    #
    #     # Преобразуем Unix-timestamp в объект datetime в UTC
    #     # Unix-timestamp обычно в секундах
    #     expiration_datetime_utc = datetime.fromtimestamp(expires_timestamp, tz=timezone.utc)
    #
    #     # Получаем текущее время в UTC (рекомендуется для сравнения с таймштампами)
    #     current_datetime_utc = datetime.now(timezone.utc)
    #
    #     print(f"\n--- Проверка куки: '{cookie_name}' ---")
    #     print(f"Дата истечения срока действия куки (UTC): {expiration_datetime_utc}")
    #     print(f"Текущая дата и время (UTC):           {current_datetime_utc}")
    #
    #     if expiration_datetime_utc > current_datetime_utc:
    #         print(f"Статус: Куки '{cookie_name}' действительна (истекает через {expiration_datetime_utc - current_datetime_utc}).")
    #     elif expiration_datetime_utc < current_datetime_utc:
    #         print(f"Статус: Куки '{cookie_name}' истекла (истекла {current_datetime_utc - expiration_datetime_utc} назад).")
    #     else:
    #         print(f"Статус: Куки '{cookie_name}' истекает прямо сейчас.")

# Вызываем функцию для проверки
check_cookie_expiration(json_data)
# check_cookie_expiration("state.json")