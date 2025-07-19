import allure
from playwright.sync_api import Page

from ..elements.element_factory import ElementFactory
from .base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.url = "https://www.saucedemo.com/"  # вынест базовый URL. А здесь его складывать с path. В данном случае ничего складывать не нужно, просто БэйсУрл буду использовать
        el = ElementFactory(page)
        self.username_input = el.text_input("#user-name")
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

    # мб создать подметоды login_with_valid_credential и т.д. Тогда сюда можно будет еще вынести чать кода и сами тесты станут ЧИЩЕ
    
    @allure.step("check if login was successful")
    def expect_login_is_successful(self):
        with allure.step(f"expect current page is inventory"):
            self.expect_current_page_url_have("https://www.saucedemo.com/inventory.html")

    @allure.step("check if login failed")
    def expect_login_failed(self):
        with allure.step("expect there is an error message"):
            self.error_message.should_be_visible()
