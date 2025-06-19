import allure

from ..pages.login_page import LoginPage

VALID_USERNAME = "standard_user"
VALID_PASSWORD = "secret_sauce"
INVALID_USERNAME = "blablabla"
INVALID_PASSWORD = "blablabla"


@allure.epic("UI")
@allure.feature("Login")
class TestLogin:
    def test_user_successfully_login_with_valid_credentials(self, login_page: LoginPage):
        login_page.login(VALID_USERNAME, VALID_PASSWORD)
        login_page.expect_login_is_successful()

    def test_user_can_not_login_with_invalid_username(self, login_page: LoginPage):
        login_page.login(INVALID_USERNAME, VALID_PASSWORD)
        login_page.expect_error_message()

    def test_user_can_not_login_with_invalid_password(self, login_page: LoginPage):
        login_page.login(VALID_USERNAME, INVALID_PASSWORD)
        login_page.expect_error_message()
