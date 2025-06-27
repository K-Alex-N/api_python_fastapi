import allure
from playwright.async_api import expect, Page, Locator


class BaseElement:
    def __init__(self, page: Page, selector: str):
        self.page = page
        self.selector = selector
        self.locator: Locator = page.locator(selector)

    @allure.step("expect to be visible")
    async def should_be_visible(self):
        with allure.step(f"expect {self.selector} is visible"):
            await expect(self.locator).to_be_visible()

    @allure.step("expect to be enabled")
    async def should_be_enabled(self):
        with allure.step(f"expect {self.selector} is enabled"):
            await expect(self.locator).to_be_enabled()


# Mixins

class ClickableElement(BaseElement):

    @allure.step("click element")
    async def click(self):
        """Click on element. If more than 1 element an error raises"""
        await self.should_be_visible()
        await self.should_be_enabled()
        await self.locator.click()

    @allure.step("click first element")
    async def click_first(self):
        """Clicks on the first element found."""
        await self.should_be_visible()
        await self.should_be_enabled()
        await self.locator.first.click()
