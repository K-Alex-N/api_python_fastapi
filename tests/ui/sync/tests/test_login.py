import allure
import pytest

from ..pages.login_page import LoginPage

VALID_USERNAME = "standard_user"
VALID_PASSWORD = "secret_sauce"


@allure.epic("UI")
@allure.feature("Sync")
@allure.story("Login")
class TestLogin:

    @pytest.mark.parametrize(
        "is_test, user, password",
        [
            ("positive", VALID_USERNAME, VALID_PASSWORD),
            ("-negative", VALID_USERNAME, "wrong_password"),
            ("-negative", VALID_USERNAME, ""),
            ("-negative", "wrong_username", VALID_PASSWORD),
            ("-negative", "", VALID_PASSWORD),
        ]
    )
    def test_login(self, is_test, user, password, login_page: LoginPage) -> None:
        login_page.login(user, password)
        if is_test == "positive":
            login_page.expect_login_is_successful()
        else:
            login_page.expect_login_failed()
