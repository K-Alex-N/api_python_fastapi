import allure
from playwright.sync_api import Locator, Page, expect


class BaseElement:
    def __init__(self, page: Page, selector: str) -> None:
        self.page = page
        self.selector = selector
        self.locator: Locator = page.locator(selector)

    @allure.step("expect to be visible")
    def should_be_visible(self) -> None:
        with allure.step(f"expect {self.selector} is visible"):
            expect(self.locator).to_be_visible()

    @allure.step("expect to be enabled")
    def should_be_enabled(self) -> None:
        with allure.step(f"expect {self.selector} is enabled"):
            expect(self.locator).to_be_enabled()


class ClickableElement(BaseElement):
    def click(self) -> None:
        """Click on element. If more than 1 element an error raises"""
        with allure.step(f"Click element {self.selector}"):
            self.should_be_visible()
            self.should_be_enabled()
            self.locator.click()

    def click_first(self) -> None:
        """Clicks on the first element found."""
        with allure.step(f"Click element {self.selector}"):
            self.should_be_visible()
            self.should_be_enabled()
            self.locator.first.click()
