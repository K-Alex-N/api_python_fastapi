import allure
from playwright.sync_api import Page

from ..components.menu_component import MenuComponent
from ..elements.element_factory import ElementFactory
from .base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.url = self.base_url + "/"
        el = ElementFactory(page)
        self.username_input = el.text_input("#user-name")
        self.password_input = el.text_input("#password")
        self.login_button = el.button("#login-button")
        self.error_message = el.text_element("[data-test='error']")
        self.menu = MenuComponent(page)

    @allure.step("open login page")
    def open(self) -> None:
        self.goto(self.url)

    @allure.step("login")
    def login(self, username: str, password: str) -> None:
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    @allure.step("check if login was successful")
    def expect_login_is_successful(self) -> None:
        with allure.step("Expect current page is inventory"):
            self.expect_page_have_url("https://www.saucedemo.com/inventory.html")

    @allure.step("check if login failed")
    def expect_login_failed(self) -> None:
        with allure.step("Expect there is an error message"):
            self.error_message.should_be_visible()
        with allure.step("Expect current page remain the same"):
            self.expect_page_have_url("https://www.saucedemo.com/")

    @allure.step("Проверить отсутствие меню на странице логина")
    def menu_should_not_be_visible(self) -> None:
        assert not self.menu.is_visible(), "Меню не должно отображаться на странице логина!"
