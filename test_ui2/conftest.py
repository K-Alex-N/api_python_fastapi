# @pytest.fixture
# @pytest.mark.asyncio  !!!!!!!!!!!!!
# async def my_async_fixture():
#     print("\n--- Асинхронная фикстура: подготовка ---")
#     yield "async_data"
#     print("--- Асинхронная фикстура: очистка ---")
#
# @pytest.mark.asyncio
# async def test_with_async_fixture(my_async_fixture):
#     print(f"Использую данные из фикстуры: {my_async_fixture}")
#     assert my_async_fixtur
#     e == "async_data"
import os

# import pytest
# from playwright.sync_api import sync_playwright
#
# @pytest.fixture(scope="function")
# def page():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=True)
#         context = browser.new_context()
#         page = context.new_page()
#         yield page
#         browser.close()


import pytest
from playwright.async_api import async_playwright
from playwright.sync_api import sync_playwright
import allure

HEADLESS = bool(os.getenv("HEADLESS", False))
SLOW_MO = int(os.getenv("SLOW_MO", 200))

STORAGE_PATH = "state.json"

# @pytest.fixture(scope="package", autouse=True) # что будет если scope="session" поставить - интересно как файлы Конфтест разные взаимодействуют
@pytest.fixture(scope="session", autouse=True) # что будет если scope="session" поставить - интересно как файлы Конфтест разные взаимодействуют
def ensure_login_state():
    if os.path.exists(STORAGE_PATH):
        # Состояние уже сохранено — логин не требуется.
        return

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=HEADLESS, slow_mo=SLOW_MO)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://www.saucedemo.com/")
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")

        # assert page.get_current_url() == "https://www.saucedemo.com/inventory.html"
        assert page.url == "https://www.saucedemo.com/inventory.html"
        # page.wait_for_selector("#dashboard")  # жди элемент после логина

        page.context.storage_state(path=STORAGE_PATH)
        browser.close()


@pytest.fixture(scope="session")
# async def page():
def page():
#     async with async_playwright() awith async_playwright() as p:
    with sync_playwright() as p:
#         browser = await p.chromium.launch(headless=True)
        browser = p.chromium.launch(headless=HEADLESS, slow_mo=SLOW_MO)
#         context = await browser.new_context()
        context = browser.new_context(storage_state=STORAGE_PATH)
#         page = await context.new_page()
        page = context.new_page()
        yield page
#         await browser.close()
        browser.close()

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