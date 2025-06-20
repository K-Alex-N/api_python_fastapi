import os

import pytest
from playwright.sync_api import sync_playwright

from .pages.login_page import LoginPage
from .pages.inventory_page import InventoryPage

HEADLESS = bool(os.getenv("HEADLESS", False))
SLOW_MO = int(os.getenv("SLOW_MO", 0))

STORAGE_PATH = "state.json"


# @pytest.fixture(scope="package", autouse=True) # что будет если scope="session" поставить - интересно как файлы Конфтест разные взаимодействуют
@pytest.fixture(scope="session", autouse=True)
def ensure_login_state():
    if os.path.exists(STORAGE_PATH):
        return  # Состояние уже сохранено — вход не требуется.

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
