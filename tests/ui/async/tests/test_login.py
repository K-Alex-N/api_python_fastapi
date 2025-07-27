import allure
import pytest
from ..pages.login_page import LoginPage

VALID_USERNAME = "standard_user"
VALID_PASSWORD = "secret_sauce"
INVALID_USERNAME = "blablabla"
INVALID_PASSWORD = "blablabla"


@allure.epic("UI_async")
@allure.feature("Login_async")
@pytest.mark.asyncio
class TestLogin:

    async def test_successful_login_async(self, login_page: LoginPage):
        """Test that user can successfully log in with valid credentials"""
        await login_page.login(VALID_USERNAME, VALID_PASSWORD)
        await login_page.expect_login_is_successful()

    async def test_failed_login_with_invalid_username_async(self, login_page: LoginPage):
        """Test that user can not log in with invalid username"""
        await login_page.login(INVALID_USERNAME, VALID_PASSWORD)
        await login_page.expect_login_failed()

    async def test_failed_login_with_invalid_password_async(self, login_page: LoginPage):
        """Test that user can not log in with invalid password"""
        await login_page.login(VALID_USERNAME, INVALID_PASSWORD)
        await login_page.expect_login_failed()
