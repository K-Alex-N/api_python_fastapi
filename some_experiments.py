# 📦 Полный шаблон для Pytest + Playwright + Allure + Docker

# ----------------------
# 📁 Структура проекта
# ----------------------
# .
# ├── app/
# │   ├── tests/               # Pytest тесты
# │   ├── pages/               # Page Object классы
# │   ├── elements/            # Элементы UI (TextInput, Button)
# │   └── __init__.py
# ├── entrypoint.sh           # Скрипт запуска
# ├── send_report.py          # Отправка Allure отчёта
# ├── conftest.py             # Общие фикстуры (включая логин)
# ├── requirements.txt
# ├── Dockerfile
# ├── docker-compose.yml
# └── .env

# ----------------------
# app/pages/login_page.py
# ----------------------
from app.pages.base_page import BasePage
from app.elements.text_input import TextInput
from app.elements.button import Button

class LoginPage(BasePage):
    URL = "https://example.com/login"

    def __init__(self, page):
        super().__init__(page)
        self.username = TextInput(page, "#username")
        self.password = TextInput(page, "#password")
        self.login_button = Button(page, "#login")

    async def open(self):
        await self.page.goto(self.URL)

    async def login(self, username, password):
        await self.username.fill(username)
        await self.password.fill(password)
        await self.login_button.click()

# ----------------------
# app/pages/base_page.py
# ----------------------
class BasePage:
    def __init__(self, page):
        self.page = page

    def el(self, selector: str):
        return self.page.locator(selector)

# ----------------------
# app/elements/text_input.py
# ----------------------
from playwright.async_api import expect

class TextInput:
    def __init__(self, page, selector):
        self.locator = page.locator(selector)

    async def fill(self, value):
        await expect(self.locator).to_be_visible()
        await self.locator.fill(value)

# ----------------------
# app/elements/button.py
# ----------------------
from playwright.async_api import expect

class Button:
    def __init__(self, page, selector):
        self.locator = page.locator(selector)

    async def click(self):
        await expect(self.locator).to_be_visible()
        await expect(self.locator).to_be_enabled()
        await self.locator.click()

# ----------------------
# app/tests/test_login.py
# ----------------------
import pytest
from app.pages.login_page import LoginPage

@pytest.mark.asyncio
async def test_login_success(logged_in_context):
    page = await logged_in_context.new_page()
    login_page = LoginPage(page)
    await login_page.open()
    await login_page.login("user", "pass")
    assert "/dashboard" in page.url
    await page.close()

# остальные файлы остаются без изменений
# conftest.py, Dockerfile, docker-compose.yml и др.
