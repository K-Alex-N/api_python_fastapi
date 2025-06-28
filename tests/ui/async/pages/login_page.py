import allure
from playwright.async_api import Page

from ..elements.element_factory import ElementFactory
from .base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.url = "https://www.saucedemo.com/"
        el = ElementFactory(page)
        self.username_input = el.text_input("#user-name")
        self.password_input = el.text_input("#password")
        self.login_button = el.button("#login-button")
        self.error_message = el.text_element("[data-test='error']")

    @allure.step("open login page")
    async def open(self):
        await self.goto(self.url)

    @allure.step("login")
    async def login(self, username: str, password: str):
        await self.username_input.fill(username)
        await self.password_input.fill(password)
        await self.login_button.click()

    @allure.step("check if login was successful")
    async def expect_login_is_successful(self):
        with allure.step("expect current page is inventory"):
            await self.expect_current_page_url_have("https://www.saucedemo.com/inventory.html")

    @allure.step("check if login failed")
    async def expect_login_failed(self):
        with allure.step("expect there is an error message"):
            await self.error_message.should_be_visible()
