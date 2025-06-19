import allure
from playwright.sync_api import expect


class BaseElement:
    def __init__(self, page, selector):
        self.page = page
        self.selector = selector
        self.locator = page.locator(selector)

    @allure.step("expect to be visible")
    def should_be_visible(self):
        expect(self.locator).to_be_visible()

    @allure.step("expect to be enabled")
    def should_be_enabled(self):
        expect(self.locator).to_be_enabled()


# Mixins


class ClickableMixin:

    def click(self):
        with allure.step(f"Click element {self.selector}"):
            self.should_be_visible()
            self.should_be_enabled()
            self.locator.click()


# Elements


class TextInput(BaseElement):

    def fill(self, value):
        with allure.step(f"Fill input {self.selector} with value: {value}"):
            self.should_be_visible()
            self.locator.fill(value)


class Button(ClickableMixin, BaseElement):
    pass


class Text(BaseElement):
    pass

    # def text(self):
    #     self.should_be_visible()
    #     return self.locator.inner_text()
    #
    # def should_have_text(self, expected: str):
    #     self.should_be_visible()
    #     self.log_action(f"Проверка текста ошибки: ожидается '{expected}'")
    #     expect(self.locator).to_have_text(expected)

class Dropdown(BaseElement):

    def select(self, value):
        self.should_be_visible()
        self.locator.select_option(value)


class Checkbox(BaseElement):

    def check(self):
        self.should_be_visible()
        if not self.locator.is_checked():
            self.locator.check()

    def uncheck(self):
        self.should_be_visible()
        if self.locator.is_checked():
            self.locator.uncheck()

    def is_checked(self):
        return self.locator.is_checked()


class Link(ClickableMixin, BaseElement):

    def href(self):
        return self.locator.get_attribute("href")
