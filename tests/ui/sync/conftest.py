import json
import os
from datetime import datetime

import allure
import pytest
from playwright.sync_api import sync_playwright, Page

from .pages.login_page import LoginPage
from .pages.inventory_page import InventoryPage

HEADLESS = bool(os.getenv("HEADLESS", True))
SLOW_MO = int(os.getenv("SLOW_MO", 0))

STORAGE_PATH = "state.json"


@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=HEADLESS, slow_mo=SLOW_MO)
        context = browser.new_context(storage_state=STORAGE_PATH)
        page = context.new_page()
        yield page
        browser.close()


@pytest.fixture
def login_page(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    yield login_page


@pytest.fixture
def inventory_page(page: Page):
    inventory_page = InventoryPage(page)
    inventory_page.open()
    yield inventory_page


@pytest.fixture(scope="session", autouse=True)
def ensure_login_state():
    if os.path.exists(STORAGE_PATH):
        # check expires time in cookies
        with open(STORAGE_PATH) as f:
            data = json.load(f)

        expires_time = data["cookies"][0]["expires"]
        now = datetime.now().timestamp()
        if expires_time - now > 20:  # 20 секунд должно хватить на тесты
            # if expires_time - now > 9999:  # чтобы всегда новый фалл получать, для чистоты эксперимента
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


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page", None)
        if page:
            screenshot = f"allure-results/screenshot-{item.name}.png"
            page.screenshot(path=screenshot)
            allure.attach.file(screenshot, name="screenshot", attachment_type=allure.attachment_type.PNG)
