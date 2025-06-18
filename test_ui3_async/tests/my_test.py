# @pytest.mark.asyncio
import allure

from test_ui.pages.page_factory import PageFactory


@allure.title("Успешный вход")
async def test_valid_login(page):
# async def test_valid_login(page):
    login_page = PageFactory(page).get_page("login")
    # await login_page.open()
    login_page.open()
    # await login_page.login("standard_user", "secret_sauce")
    login_page.login("standard_user", "secret_sauce")

    # assert await login_page.get_current_url() == "https://www.saucedemo.com/inventory.html"
    assert await login_page.get_current_url() == "https://www.saucedemo.com/inventory.html"
