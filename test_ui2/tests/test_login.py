import allure

from test_ui2.pages.login_page import LoginPage

VALID_USERNAME = "standard_user"
VALID_PASSWORD = "secret_sauce"
INVALID_USERNAME = "blablabla"
INVALID_PASSWORD = "blablabla"


@allure.epic("UI")
@allure.feature("Login")
def test_user_successfully_login_with_valid_credentials(page):
    """description of test"""

    login_page = LoginPage(page)
    login_page.open()

    login_page.login(VALID_USERNAME, VALID_PASSWORD)

    # assert login_page.is_login_successful(), "Login failed!"
    # login_page.wait_for_title("Swag Labs")
    login_page.wait_for_url("https://www.saucedemo.com/inventory.html")


def test_login_with_token(page):
    pass



# @allure.epic("UI")
# @allure.feature("Login")
# def test_user_can_not_login_with_invalid_username(page):
#     """description of test"""
#
#     login_page = LoginPage(page)
#     login_page.open()
#
#     login_page.login(INVALID_USERNAME, VALID_PASSWORD)
#
#     assert login_page.is_error_message_present()
#     assert login_page.get_current_url() == "https://www.saucedemo.com/"
#
#
# @allure.epic("UI")
# @allure.feature("Login")
# def test_user_can_not_login_with_invalid_password(page):
#     """description of test"""
#
#     login_page = LoginPage(page)
#     login_page.open()
#
#     login_page.login(VALID_USERNAME, INVALID_PASSWORD)
#
#     assert login_page.is_error_message_present()
#     assert login_page.get_current_url() == "https://www.saucedemo.com/"
