# from playwright.sync_api import Page
#
# class LoginPage:
#     def __init__(self, page: Page):
#         self.page = page
#         self.username_input = page.locator("#user-name")
#         self.password_input = page.locator("#password")
#         self.login_button = page.locator("#login-button")
#         self.error_message = page.locator("[data-test='error']")
#
#     def navigate(self):
#         self.page.goto("https://www.saucedemo.com/")
#
#     def login(self, username: str, password: str):
#         self.username_input.fill(username)
#         self.password_input.fill(password)
#         self.login_button.click()
#
#     def get_error_text(self) -> str:
#         return self.error_message.inner_text()

# после переделки да. сделай Разбить на BasePage + LoginPage и Добавить паттерн PageFactory

# from .base_page import BasePage
#
# class LoginPage(BasePage):
#     URL = "https://www.saucedemo.com/"
#     USERNAME_INPUT = "#user-name"
#     PASSWORD_INPUT = "#password"
#     LOGIN_BUTTON = "#login-button"
#     ERROR_MESSAGE = "[data-test='error']"
#
#     def open(self):
#         self.navigate(self.URL)
#
#     def login(self, username: str, password: str):
#         self.fill(self.USERNAME_INPUT, username)
#         self.fill(self.PASSWORD_INPUT, password)
#         self.click(self.LOGIN_BUTTON)
#
#     def get_error_text(self) -> str:
#         return self.get_text(self.ERROR_MESSAGE)


from .base_page import BasePage

class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"
    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_MESSAGE = "[data-test='error']"

    async def open(self):
        await self.navigate(self.URL)

    async def login(self, username: str, password: str):
        await self.fill(self.USERNAME_INPUT, username)
        await self.fill(self.PASSWORD_INPUT, password)
        await self.click(self.LOGIN_BUTTON)

    async def get_error_text(self) -> str:
        return await self.get_text(self.ERROR_MESSAGE)
