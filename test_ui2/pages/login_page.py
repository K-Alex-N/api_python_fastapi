import allure
from playwright.sync_api import expect

from .elements import TextInput, Button
from .base_page import BasePage


class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"
    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_MESSAGE = "[data-test='error']"

    def __init__(self, page):
        super().__init__(page)
        self.url = "https://www.saucedemo.com/"
        self.username_input = TextInput(page, "#user-name")
        self.password_input = TextInput(page, "#password")
        self.login_button = Button(page, "#login-button")

        self.error_message = page.locator("[data-test='error']")

    @allure.step("open login page")
    def open(self):
        self.navigate_to(self.URL)

    # @allure.step("login")
    # @allure.step
    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    # @allure.step("login")
    # def login(self, username: str, password: str):
    #     self.fill(self.USERNAME_INPUT, username)
    #     self.fill(self.PASSWORD_INPUT, password)
    #     self.click(self.LOGIN_BUTTON)

    # @allure.step("check if login is successful")
    def expect_login_is_successful(self):
        self.wait_for_url("https://www.saucedemo.com/inventory.html")

    # @allure.step("check error message")
    def expect_error_message(self):
        # expect(self.ERROR_MESSAGE).is_present()
        expect(self.error_message).to_be_visible()

    # def get_error_text(self) -> str:
    #     return self.get_text(self.ERROR_MESSAGE)

# from base_page import BasePage
#
# class LoginPage(BasePage):
#     URL = "https://www.saucedemo.com/"
#     USERNAME_INPUT = "#user-name"
#     PASSWORD_INPUT = "#password"
#     LOGIN_BUTTON = "#login-button"
#     ERROR_MESSAGE = "[data-test='error']"
#
#     # async def open(self):
#     def open(self):
#         # await self.navigate(self.URL)
#         self.navigate_to(self.URL)
#
#     # async def login(self, username: str, password: str):
#     def login(self, username: str, password: str):
#         # await self.fill(self.USERNAME_INPUT, username)
#         self.fill(self.USERNAME_INPUT, username)
# #         await self.fill(self.PASSWORD_INPUT, password)
#         self.fill(self.PASSWORD_INPUT, password)
# #         await self.click(self.LOGIN_BUTTON)
#         self.click(self.LOGIN_BUTTON)

# async def get_error_text(self) -> str:
# def get_error_text(self) -> str:
#     # return await self.get_text(self.ERROR_MESSAGE)
#     return self.get_text(self.ERROR_MESSAGE)
