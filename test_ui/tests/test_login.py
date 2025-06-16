# from tests.test_ui.pages.login_page import LoginPage
#
#
# def test_valid_login(page):
#     login_page = LoginPage(page)
#     login_page.navigate()
#     login_page.login("standard_user", "secret_sauce")
#
#     # Проверим, что попали на страницу продуктов
#     assert page.url == "https://www.saucedemo.com/inventory.html"
#
# def test_invalid_login(page):
#     login_page = LoginPage(page)
#     login_page.navigate()
#     login_page.login("wrong_user", "wrong_pass")
#
#     # Проверка текста ошибки
#     assert "Username and password do not match" in login_page.get_error_text()
#


# # после переделки да. сделай Разбить на BasePage + LoginPage и Добавить паттерн PageFactory


# from tests.test_ui.pages.page_factory import PageFactory
#
# def test_valid_login(page):
#     factory = PageFactory(page)
#     login_page = factory.get_page("login")
#
#     login_page.open()
#     login_page.login("standard_user", "secret_sauce")
#     assert login_page.get_current_url() == "https://www.saucedemo.com/inventory.html"
#
# def test_invalid_login(page):
#     factory = PageFactory(page)
#     login_page = factory.get_page("login")
#
#     login_page.open()
#     login_page.login("wrong_user", "wrong_pass")
#     assert "Username and password do not match" in login_page.get_error_text()

import pytest
import allure
from tests.test_ui.pages.page_factory import PageFactory

@pytest.mark.asyncio
@allure.title("Успешный вход")
async def test_valid_login(page):
    login_page = PageFactory(page).get_page("login")
    await login_page.open()
    await login_page.login("standard_user", "secret_sauce")

    assert await login_page.get_current_url() == "https://www.saucedemo.com/inventory.html"

@pytest.mark.asyncio
@allure.title("Неверный логин")
async def test_invalid_login(page):
    login_page = PageFactory(page).get_page("login")
    await login_page.open()
    await login_page.login("wrong_user", "wrong_pass")

    error_text = await login_page.get_error_text()
    assert "Username and password do not match" in error_text

@pytest.mark.asyncio
@allure.title("Успешный логин и переход в корзину")
async def test_login_and_cart(page):
    factory = PageFactory(page)
    login = factory.get_page("login")
    inventory = factory.get_page("inventory")
    cart = factory.get_page("cart")

    await login.open()
    await login.login("standard_user", "secret_sauce")

    assert await login.get_current_url() == inventory.URL

    await inventory.go_to_cart()
    assert await cart.get_current_url() == cart.URL