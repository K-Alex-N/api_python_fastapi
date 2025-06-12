import asyncio
import os

import pytest
from playwright.async_api import Playwright, async_playwright, expect

HEADLESS = bool(os.getenv("HEADLESS", False))
SLOW_MO = os.getenv("SLOW_MO", 200)

VALID_USERNAME = "standard_user"
VALID_PASSWORD = "secret_sauce"
INVALID_USERNAME = "invalid user"
INVALID_PASSWORD = "invalid pass"


@pytest.mark.asyncio
async def test_user_successfully_logs_in_with_valid_credentials():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=HEADLESS, slow_mo=SLOW_MO)
        page = await browser.new_page()

        # мб проставить аллюр метки --- "Открываем ..."
        await page.goto("https://www.saucedemo.com/")

        # locators
        # pas ---
        # pas --
        # but -
        # если не верный логин или пароль    .error-message-container

        print("Ввожу username...")
        await page.fill("#user-name", "standard_user")
        await page.fill("#password", "secret_sauce")
        await page.click("#login-button")

        await expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

        # 6. Ожидание загрузки страницы результатов
        # Можно ждать конкретного элемента на странице результатов
        # await page.wait_for_selector('#search')  # Ждем появления блока с результатами поиска
        # print(f"Заголовок страницы результатов: {await page.title()}")

        # 7. Извлечение заголовков первых нескольких результатов поиска
        # print("\nЗаголовки первых 5 результатов поиска:")
        # Ищем все элементы с классом 'LC20lb MBeuO DCoPu' (это заголовки результатов)
        # locator() возвращает Locator, который может найти несколько элементов
        # all_text_contents() извлекает текст из всех найденных элементов
        # search_results_titles = await page.locator('h3').all_text_contents()
        # for i, title in enumerate(search_results_titles[:5]):  # Берем первые 5
        #     print(f"{i + 1}. {title}")

        # 8. Закрытие браузера
        print("\nЗакрываю браузер.")
        await browser.close()

        # .app_logo

        # Лучше сделать LOGOUT на следуюшей странице


@pytest.mark.asyncio
async def test_user_can_not_logs_in_with_invalid_username():
    pass


@pytest.mark.asyncio
async def test_user_can_not_logs_in_with_invalid_password():
    pass
