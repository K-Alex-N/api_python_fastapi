import allure
from playwright.sync_api import expect


class TextInput:
    def __init__(self, page, selector):
        self.locator = page.locator(selector)

    # @allure.step("Fill input {self.locator} with value: {value}")
    def fill(self, value):
        # expect(self.locator).to_be_visible()
        self.locator.fill(value)


class Button:
    def __init__(self, page, selector):
        self.locator = page.locator(selector)

    # @allure.step("Click element -> {self.locator}")
    def click(self):
        expect(self.locator).to_be_visible()
        expect(self.locator).to_be_enabled()
        self.locator.click()
