import pytest

from ..pages.login_page import LoginPage
from ..utils.allure_decorators import epic, feature

VALID_USERNAME = "standard_user"
VALID_PASSWORD = "secret_sauce"
INVALID_USERNAME = "wrong_username"
INVALID_PASSWORD = "wrong_password"


@epic("UI")
@feature("Login")
class TestLogin:
    def test_successful_login(self, login_page: LoginPage):
        """Test that user can successfully log in with valid credentials"""
        login_page.login(VALID_USERNAME, VALID_PASSWORD)
        login_page.expect_login_is_successful()

    @pytest.mark.parametrize("user, password", [
        (VALID_USERNAME, INVALID_PASSWORD),
        (INVALID_USERNAME, VALID_PASSWORD),
        (VALID_USERNAME, ""),
        ("", VALID_PASSWORD),
    ])
    def test_login_with_invalid_credentials(self, user, password, login_page: LoginPage):
        """Test that user can not log in with invalid credentials"""
        login_page.login(user, password)
        login_page.expect_login_failed()
