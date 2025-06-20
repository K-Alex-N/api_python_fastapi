from ..elements.element_factory import ElementFactory
from ..elements.single_element import *
from .base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.url = "https://www.saucedemo.com/"
        el = ElementFactory(page)
        self.username_input = el.text_input("#user-name")
        # self.username_input = TextInput(page, "#user-name", "поле ввода имени пользователя")

        self.password_input = el.text_input("#password")
        self.login_button = el.button("#login-button")
        self.error_message = el.text_element("[data-test='error']")

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
