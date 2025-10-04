import allure
from playwright.async_api import Page, expect


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page

    @allure.step("Go to URL -> {url}")
    async def goto(self, url: str) -> None:
        await self.page.goto(url)

    @allure.step("Reload page")
    async def reload(self) -> None:
        await self.page.reload()

    @allure.step("Back to previous page")
    async def back(self) -> None:
        await self.page.go_back()

    @allure.step("Get current URL")
    async def get_current_url(self) -> str:
        return self.page.url

    @allure.step("Expect page to have title: {title}")
    async def expect_page_have_title(self, title: str) -> None:
        await expect(self.page).to_have_title(title)

    @allure.step("Expect page URL contains: {url_part}")
    async def expect_current_page_url_have(self, url_part: str) -> None:
        await expect(self.page).to_have_url(url_part)
