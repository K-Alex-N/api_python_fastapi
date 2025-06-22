import os

import pytest
from playwright.sync_api import sync_playwright

from .pages.login_page import LoginPage
from .pages.inventory_page import InventoryPage

HEADLESS = bool(os.getenv("HEADLESS", True))
SLOW_MO = int(os.getenv("SLOW_MO", 0))

STORAGE_PATH = "state.json"


# @pytest.fixture(scope="package", autouse=True) # что будет если scope="session" поставить - интересно как файлы Конфтест разные взаимодействуют
@pytest.fixture(scope="session", autouse=True)
def ensure_login_state():
    if os.path.exists(STORAGE_PATH):
        # check expires time in cookies
        with open(STORAGE_PATH) as f:
            data = json.load(f)

        expires_time = data["cookies"][0]["expires"]
        now = datetime.now().timestamp()
        if expires_time - now > 20: # 20 секунд должно хватить на тесты
            return

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=HEADLESS, slow_mo=SLOW_MO)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://www.saucedemo.com/")
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")
        assert page.url == "https://www.saucedemo.com/inventory.html"

        page.context.storage_state(path=STORAGE_PATH)
        browser.close()


# Если с путями к файлу будут проблемы в Докере, то мб вот это попробовать

# @pytest.fixture(scope="session")
# async def login_and_save_storage(tmp_path_factory):
#     path = tmp_path_factory.mktemp("auth") / "state.json"
#     async with async_playwright() as p:
#         browser = await p.chromium.launch()
#         page = await browser.new_page()
#         await page.goto("https://example.com/login")
#         await page.fill("#username", "user")
#         await page.fill("#password", "pass")
#         await page.click("#login")
#         await page.context.storage_state(path=path)
#         await browser.close()
#     return path


@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=HEADLESS, slow_mo=SLOW_MO)
        context = browser.new_context(storage_state=STORAGE_PATH)
        page = context.new_page()
        yield page
        browser.close()


@pytest.fixture
def login_page(page):
    login_page = LoginPage(page)
    login_page.open()
    yield login_page


@pytest.fixture
def inventory_page(page):
    inventory_page = InventoryPage(page)
    inventory_page.open()
    yield inventory_page


# # Хук: скриншоты при падении
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     rep = outcome.get_result()
#     if rep.when == "call" and rep.failed:
#         page = item.funcargs.get("page", None)
#         if page:
#             screenshot = f"screenshot-{item.name}.png"
#             page.screenshot(path=screenshot)
#             allure.attach.file(screenshot, name="screenshot", attachment_type=allure.attachment_type.PNG)


# ______________________________________
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
# check_cookie_expiration(json_data)
# check_cookie_expiration("state.json") # из файла пока не вызывается
