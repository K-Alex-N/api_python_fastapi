# from tests.ui.pages.login_page import LoginPage
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


from tests.ui.pages.page_factory import PageFactory

def test_valid_login(page):
    factory = PageFactory(page)
    login_page = factory.get_page("login")

    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    assert login_page.get_current_url() == "https://www.saucedemo.com/inventory.html"

def test_invalid_login(page):
    factory = PageFactory(page)
    login_page = factory.get_page("login")

    login_page.open()
    login_page.login("wrong_user", "wrong_pass")
    assert "Username and password do not match" in login_page.get_error_text()

