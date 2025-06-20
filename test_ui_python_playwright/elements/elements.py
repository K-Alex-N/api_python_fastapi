import allure
from playwright.sync_api import expect

from .base import BaseElement, ClickableMixin


class TextInput(BaseElement):
    """
    если ты хочешь работать именно с полями ввода (<input type="text">)
    """

    def fill(self, value):
        with allure.step(f"Fill input {self.selector} with value: {value}"):
            self.should_be_visible()
            self.locator.fill(value)

    # def clear(self):
    #     self.locator.clear()


class Button(ClickableMixin, BaseElement):
    pass


class TextElement(BaseElement):
    """
    если хочешь получить доступ к элементам, содержащим
    текст (<div>, <span>, и т.д.)
    """

    def text(self):
        with allure.step("Getting inner text"):
            self.should_be_visible()
            return self.locator.inner_text()

    def should_have_text(self, expected: str):
        with allure.step(f"Text should have {expected}"):
            self.should_be_visible()
            expect(self.locator).to_have_text(expected)


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
