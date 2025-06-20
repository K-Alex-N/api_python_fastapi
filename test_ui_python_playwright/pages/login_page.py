from ..elements.elements import *
from .base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.url = "https://www.saucedemo.com/"
        self.username_input = TextInput(page, "#user-name", "поле ввода имени пользователя")
        self.password_input = TextInput(page, "#password")
        self.login_button = Button(page, "#login-button")
        self.error_message = TextElement(page, "[data-test='error']")

    @allure.step("open login page")
    def open(self):
        self.goto(self.url)

    @allure.step("login")
    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    @allure.step("check if login was successful")
    def expect_login_is_successful(self):
        self.expect_current_page_url_have("https://www.saucedemo.com/inventory.html")

    @allure.step("check error message")
    def expect_error_message(self):
        self.error_message.should_be_visible()
