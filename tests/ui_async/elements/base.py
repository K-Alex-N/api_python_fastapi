import allure
from playwright.async_api import Locator, Page, expect


class BaseElement:
    def __init__(self, page: Page, selector: str) -> None:
        self.page = page
        self.selector = selector
        self.locator: Locator = page.locator(selector)

    async def should_be_visible(self) -> None:
        with allure.step(f"expect {self.selector} is visible"):
            await expect(self.locator).to_be_visible()

    async def should_be_enabled(self) -> None:
        with allure.step(f"expect {self.selector} is enabled"):
            await expect(self.locator).to_be_enabled()


class ClickableElement(BaseElement):
    async def click(self) -> None:
        """Click on element. If more than 1 element an error raises"""
        with allure.step(f"Click element {self.selector}"):
            await self.should_be_visible()
            await self.should_be_enabled()
            await self.locator.click()

    async def click_first(self) -> None:
        """Clicks on the first element found."""
        with allure.step(f"Click element {self.selector}"):
            await self.should_be_visible()
            await self.should_be_enabled()
            await self.locator.first.click()
