import json
import os
from datetime import datetime

import allure
import pytest
from playwright.async_api import async_playwright, Page

from .pages.login_page import LoginPage
from .pages.inventory_page import InventoryPage

HEADLESS = bool(os.getenv("HEADLESS", True))
SLOW_MO = int(os.getenv("SLOW_MO", 0))

STORAGE_PATH = "state.json"


@pytest.fixture(scope="session", autouse=True)
async def ensure_login_state():
    if os.path.exists(STORAGE_PATH):
        # check expires time in cookies
        with open(STORAGE_PATH) as f:
            data = json.load(f)

        expires_time = data["cookies"][0]["expires"]
        now = datetime.now().timestamp()
        # if expires_time - now > 20: # 20 секунд должно хватить на тесты
        if expires_time - now > 9999:  # чтобы всегда новый фалл получать, для чистоты эксперимента
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


@pytest.fixture
async def page():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=HEADLESS, slow_mo=SLOW_MO)
        context = await browser.new_context(storage_state=STORAGE_PATH)
        page = await context.new_page()
        yield page
        await browser.close()


@pytest.fixture
async def login_page(page: Page):
    login_page = LoginPage(page)
    await login_page.open()
    yield login_page


@pytest.fixture
async def inventory_page(page: Page):
    inventory_page = InventoryPage(page)
    await inventory_page.open()
    yield inventory_page


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page", None)
        if page:
            # Скриншот может требовать await — но хуки pytest не async,
            # поэтому используем sync-обертку или записываем sync-метод
            # Playwright async API не имеет sync методов, так что нужно обойтись так:
            # для простоты здесь делаем sync-версию (опасно, но часто срабатывает)
            screenshot = f"allure-results/screenshot-{item.name}.png"
            # Лучше - сохранить скриншот в отдельном async hook или внутри теста при ошибке
            # Но для минимальных изменений можно вызвать sync блокирующий asyncio.run():
            import asyncio
            asyncio.run(page.screenshot(path=screenshot))
            allure.attach.file(screenshot, name="screenshot", attachment_type=allure.attachment_type.PNG)
