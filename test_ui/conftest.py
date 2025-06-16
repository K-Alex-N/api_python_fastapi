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
import allure


@pytest.fixture
async def page():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        yield page
        await browser.close()

# Хук: скриншоты при падении
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page", None)
        if page:
            screenshot = f"screenshot-{item.name}.png"
            page.screenshot(path=screenshot)
            allure.attach.file(screenshot, name="screenshot", attachment_type=allure.attachment_type.PNG)