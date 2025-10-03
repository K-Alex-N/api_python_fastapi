import asyncio
import json
import os
from datetime import datetime

import allure
import pytest
import pytest_asyncio
from playwright.async_api import async_playwright, Page

from .pages.login_page import LoginPage
from .pages.inventory_page import InventoryPage

HEADLESS = bool(os.getenv("HEADLESS", True))
SLOW_MO = int(os.getenv("SLOW_MO", 0))

STORAGE_PATH = "state.json"


@pytest_asyncio.fixture(scope="function", autouse=True)
async def ensure_login_state():
    if os.path.exists(STORAGE_PATH):
        # check expires time in cookies
        with open(STORAGE_PATH) as f:
            data = json.load(f)

        expires_time = data["cookies"][0]["expires"]
        now = datetime.now().timestamp()
        max_test_duration_sec = 30 # 30 секунд должно хватить на тесты
        if expires_time - now > max_test_duration_sec:
            return

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=HEADLESS, slow_mo=SLOW_MO)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto("https://www.saucedemo.com/")
        await page.fill("#user-name", "standard_user")
        await page.fill("#password", "secret_sauce")
        await page.click("#login-button")
        assert page.url == "https://www.saucedemo.com/inventory.html"

        await context.storage_state(path=STORAGE_PATH)
        await browser.close()

@pytest_asyncio.fixture
async def page(request):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=HEADLESS, slow_mo=SLOW_MO)
        context = await browser.new_context(storage_state=STORAGE_PATH)
        page = await context.new_page()

        yield page

        if request.node.rep_call.failed:
            screenshot = f"allure-results/screenshot-{request.node.name}.png"
            await page.screenshot(path=screenshot)
            allure.attach.file(screenshot, name="screenshot", attachment_type=allure.attachment_type.PNG)

        await browser.close()

@pytest_asyncio.fixture
async def login_page(page: Page):
    login_page = LoginPage(page)
    await login_page.open()
    yield login_page


@pytest_asyncio.fixture
async def inventory_page(page: Page):
    inventory_page = InventoryPage(page)
    await inventory_page.open()
    yield inventory_page


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()

    setattr(item, f"rep_{rep.when}", rep)
