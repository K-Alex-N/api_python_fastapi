import json
import os
from datetime import datetime

import allure
import pytest
import pytest_asyncio
from playwright.async_api import Page, async_playwright

from .config import HEADLESS, SLOW_MO
from .pages.inventory_page import InventoryPage
from .pages.login_page import LoginPage

HEADLESS = bool(os.getenv("HEADLESS", HEADLESS))
SLOW_MO = int(os.getenv("SLOW_MO", SLOW_MO))

STORAGE_PATH = "state.json"
TIME_FOR_TESTS_SEC = 60


@pytest_asyncio.fixture
async def page():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=HEADLESS, slow_mo=SLOW_MO)
        context = await browser.new_context(
            storage_state=STORAGE_PATH if os.path.exists(STORAGE_PATH) else None
        )
        page = await context.new_page()
        yield page
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


def is_remaining_time_in_cookies_enough_for_tests() -> bool:
    if os.path.exists(STORAGE_PATH):
        with open(STORAGE_PATH) as f:
            data = json.load(f)

        expires_time = data["cookies"][0]["expires"]
        now = datetime.now().timestamp()
        if expires_time - now > TIME_FOR_TESTS_SEC:
            return True
    return False


async def get_new_cookies() -> None:
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


@pytest_asyncio.fixture(scope="session", autouse=True)
async def ensure_login_state() -> None:
    if is_remaining_time_in_cookies_enough_for_tests():
        return

    await get_new_cookies()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page", None)
        if page:
            screenshot = f"allure-results/screenshot-{item.name}.png"
            try:
                # Для async страниц screenshot тоже async метод
                import asyncio

                if asyncio.iscoroutinefunction(page.screenshot):
                    # Создаем новый event loop для синхронного выполнения
                    try:
                        loop = asyncio.get_event_loop()
                    except RuntimeError:
                        loop = asyncio.new_event_loop()
                        asyncio.set_event_loop(loop)
                    loop.run_until_complete(page.screenshot(path=screenshot))
                else:
                    page.screenshot(path=screenshot)
                allure.attach.file(
                    screenshot,
                    name="screenshot",
                    attachment_type=allure.attachment_type.PNG,
                )
            except Exception as e:
                print(f"Failed to take screenshot: {e}")
