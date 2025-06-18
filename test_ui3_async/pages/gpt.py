# 📦 Полный шаблон для Pytest + Playwright + Allure + Docker + Page Object с elements.py

# ----------------------
# 📁 Структура проекта
# ----------------------
# .
# ├── app/
# │   ├── tests/               # Pytest тесты
# │   ├── pages/
# │   │   ├── base_page.py     # Базовая логика взаимодействия с Playwright
# │   │   ├── elements.py      # Обёртки над элементами (TextInput, Button и др.)
# │   │   └── login_page.py    # LoginPage, использующий elements
# │   └── __init__.py
# ├── entrypoint.sh
# ├── send_report.py
# ├── requirements.txt
# ├── Dockerfile
# ├── docker-compose.yml
# └── .env

# ----------------------
# app/pages/elements.py
# ----------------------
class Button:
    def __init__(self, page, locator):
        self.page = page
        self.locator = locator

    async def click(self):
        await self.page.locator(self.locator).click()

class TextInput:
    def __init__(self, page, locator):
        self.page = page
        self.locator = locator

    async def fill(self, value):
        await self.page.locator(self.locator).fill(value)

    async def clear(self):
        await self.page.locator(self.locator).fill("")

# ----------------------
# app/pages/base_page.py
# ----------------------
class BasePage:
    def __init__(self, page):
        self.page = page

# ----------------------
# app/pages/login_page.py
# ----------------------
from app.pages.base_page import BasePage
from app.pages.elements import TextInput, Button

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.username_input = TextInput(page, "#username")
        self.password_input = TextInput(page, "#password")
        self.login_button = Button(page, "#login")

    async def login(self, username, password):
        await self.username_input.fill(username)
        await self.password_input.fill(password)
        await self.login_button.click()

# ----------------------
# app/tests/test_login.py
# ----------------------
import pytest
from playwright.async_api import async_playwright
from app.pages.login_page import LoginPage

@pytest.mark.asyncio
async def test_login_success():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://example.com/login")

        login = LoginPage(page)
        await login.login("user", "pass")

        assert page.url.endswith("/dashboard")
        await browser.close()

# ----------------------
# 🧾 requirements.txt (дополнено)
# ----------------------
pytest
pytest-asyncio
playwright
allure-pytest
requests
python-dotenv

# Остальная часть проекта остаётся без изменений
# (entrypoint.sh, Dockerfile, send_report.py и т.д.)
