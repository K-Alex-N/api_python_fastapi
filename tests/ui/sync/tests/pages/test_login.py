import allure
import pytest

from tests.ui.sync.pages.login_page import LoginPage

VALID_USERNAME = "standard_user"
VALID_PASSWORD = "secret_sauce"


@allure.epic("UI")
@allure.feature("Sync")
@allure.story("Login")
class TestLogin:
    def test_login_success(self, login_page: LoginPage):
        login_page.login(VALID_USERNAME, VALID_PASSWORD)
        login_page.expect_login_is_successful()

    @pytest.mark.parametrize(
        "user, password",
        [
            (VALID_USERNAME, "wrong_password"),
            (VALID_USERNAME, ""),
            ("wrong_username", VALID_PASSWORD),
            ("", VALID_PASSWORD),
        ],
    )
    def test_login_fails(self, user, password, login_page: LoginPage):
        login_page.login(user, password)
        login_page.expect_login_failed()

    def test_menu_not_present_on_login(self, login_page: LoginPage):
        login_page.open()
        login_page.menu_should_not_be_visible()
