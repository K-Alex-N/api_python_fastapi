import allure
from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.base_url = "https://www.saucedemo.com"

    @allure.step("Go to URL -> {url}")
    def goto(self, url: str):
        self.page.goto(url)

    @allure.step("Reload page")
    def reload(self):
        self.page.reload()

    @allure.step("Back to previous page")
    def back(self):
        self.page.go_back()

    @allure.step("get current url")
    def get_current_url(self) -> str:
        return self.page.url

    @allure.step("expect page have title: {title}")
    def expect_page_have_title(self, title: str):
        expect(self.page).to_have_title(title)

    @allure.step("expect page have url: {url_part}")
    def expect_page_have_url(self, url_part: str):
        expect(self.page).to_have_url(url_part)
