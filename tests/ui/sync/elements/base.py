import allure
from playwright.sync_api import expect, Page, Locator


class BaseElement:
    def __init__(self, page: Page, selector: str):
        self.page = page
        self.selector = selector
        self.locator: Locator = page.locator(selector)

    @allure.step("expect to be visible")
    def should_be_visible(self):
        with allure.step(f"expect {self.selector} is visible"):
            expect(self.locator).to_be_visible()

    @allure.step("expect to be enabled")
    def should_be_enabled(self):
        with allure.step(f"expect {self.selector} is enabled"):
            expect(self.locator).to_be_enabled()


# Mixins

class ClickableElement(BaseElement):

    def click(self):
        """Click on element. If more than 1 element an error raises"""
        with allure.step(f"Click element {self.selector}"):
            self.should_be_visible()
            self.should_be_enabled()
            self.locator.click()

    def click_first(self):
        """Clicks on the first element found."""
        with allure.step(f"Click element {self.selector}"):
            self.should_be_visible()
            self.should_be_enabled()
            self.locator.first.click()
