import allure
from playwright.sync_api import Page, expect

from tests.ui.sync.config import BASEURL


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.base_url = BASEURL

    @allure.step("Go to URL -> {url}")
    def goto(self, url: str) -> None:
        self.page.goto(url)

    @allure.step("Reload page")
    def reload(self) -> None:
        self.page.reload()

    @allure.step("Back to previous page")
    def back(self) -> None:
        self.page.go_back()

    @allure.step("Get current url")
    def get_current_url(self) -> str:
        return self.page.url

    @allure.step("Expect page have title: {title}")
    def expect_page_have_title(self, title: str) -> None:
        expect(self.page).to_have_title(title)

    @allure.step("Expect page have url: {url_part}")
    def expect_page_have_url(self, url_part: str) -> None:
        expect(self.page).to_have_url(url_part)

    @allure.step("Take screenshot to {filename}")
    def take_screenshot(self, filename: str) -> None:
        self.page.screenshot(path=filename, full_page=True)
