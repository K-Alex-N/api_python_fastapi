from ..pages.login_page import LoginPage
from ..utils.allure_decorators import epic, feature

VALID_USERNAME = "standard_user"
VALID_PASSWORD = "secret_sauce"
INVALID_USERNAME = "blablabla"
INVALID_PASSWORD = "blablabla"


@epic("UI")
@feature("Login")
class TestLogin:
    def test_successful_login(self, login_page: LoginPage):
        """Test that user can successfully log in with valid credentials"""
        login_page.login(VALID_USERNAME, VALID_PASSWORD)
        login_page.expect_login_is_successful()

    def test_failed_login_with_invalid_username(self, login_page: LoginPage):
        """Test that user can not log in with invalid username"""
        login_page.login(INVALID_USERNAME, VALID_PASSWORD)
        login_page.expect_login_failed()

    def test_failed_login_with_invalid_password(self, login_page: LoginPage):
        """Test that user can not log in with invalid password"""
        login_page.login(VALID_USERNAME, INVALID_PASSWORD)
        login_page.expect_login_failed()
