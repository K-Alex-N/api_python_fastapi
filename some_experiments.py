# 📦 Полный шаблон для Pytest + Playwright + Allure + Docker (Sync API)

# ----------------------
# 📁 Структура проекта
# ----------------------
# .
# ├── app/
# │   ├── tests/               # Pytest тесты
# │   ├── pages/               # Page Object классы
# │   ├── elements/            # Элементы UI (TextInput, Button, Checkbox, Dropdown, Link)
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
import allure

class LoginPage(BasePage):
    URL = "https://example.com/login"

    def __init__(self, page):
        super().__init__(page)
        self.username = TextInput(page, "#username")
        self.password = TextInput(page, "#password")
        self.login_button = Button(page, "#login")

    def open(self):
        self.page.goto(self.URL)

    @allure.step("login")
    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()

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
from playwright.sync_api import expect

class TextInput:
    def __init__(self, page, selector):
        self.locator = page.locator(selector)

    def fill(self, value):
        expect(self.locator).to_be_visible()
        self.locator.fill(value)

# ----------------------
# app/elements/button.py
# ----------------------
from playwright.sync_api import expect

class Button:
    def __init__(self, page, selector):
        self.locator = page.locator(selector)

    def click(self):
        expect(self.locator).to_be_visible()
        expect(self.locator).to_be_enabled()
        self.locator.click()

# ----------------------
# app/elements/checkbox.py
# ----------------------
from playwright.sync_api import expect

class Checkbox:
    def __init__(self, page, selector):
        self.locator = page.locator(selector)

    def check(self):
        expect(self.locator).to_be_visible()
        if not self.locator.is_checked():
            self.locator.check()

    def uncheck(self):
        expect(self.locator).to_be_visible()
        if self.locator.is_checked():
            self.locator.uncheck()

    def is_checked(self):
        return self.locator.is_checked()

# ----------------------
# app/elements/dropdown.py
# ----------------------
from playwright.sync_api import expect

class Dropdown:
    def __init__(self, page, selector):
        self.locator = page.locator(selector)

    def select(self, value):
        expect(self.locator).to_be_visible()
        self.locator.select_option(value)

# ----------------------
# app/elements/link.py
# ----------------------
from playwright.sync_api import expect

class Link:
    def __init__(self, page, selector):
        self.locator = page.locator(selector)

    def click(self):
        expect(self.locator).to_be_visible()
        self.locator.click()

    def href(self):
        return self.locator.get_attribute("href")

# ----------------------
# app/tests/test_login.py
# ----------------------
import pytest
from app.pages.login_page import LoginPage
from playwright.sync_api import sync_playwright

def test_login_success():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        login_page = LoginPage(page)
        login_page.open()
        login_page.login("user", "pass")
        assert "/dashboard" in page.url
        browser.close()

# остальные файлы остаются без изменений
