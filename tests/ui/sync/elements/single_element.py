import allure
from playwright.sync_api import expect

from .base import BaseElement, ClickableElement


class TextInput(BaseElement):
    """input field (<input type="text">)"""

    @allure.step("Fill input with value: {value}")
    def fill(self, value: str) -> None:
        self.should_be_visible()
        self.locator.fill(value)

    def clear(self) -> None:
        self.locator.clear()

    def type_text(self, selector: str, value: str, delay_ms: int = 50) -> None:
        self.page.locator(selector).type(value, delay=delay_ms)


class Button(ClickableElement):
    pass


class TextElement(BaseElement):
    """elements that have text (<div>, <span> etc)"""

    @allure.step("Getting inner text")
    def text(self) -> str:
        self.should_be_visible()
        return self.locator.inner_text()

    @allure.step("Text should have {expected_text}")
    def should_have_text(self, expected_text: str) -> None:
        self.should_be_visible()
        expect(self.locator).to_have_text(expected_text)


class Dropdown(BaseElement):

    def select_by_value(self, value: str) -> None:
        self.should_be_visible()
        self.locator.select_option(value=value)

    def select_by_label(self, label: str) -> None:
        self.should_be_visible()
        self.locator.select_option(label=label)

    def get_selected_option_label(self) -> str:
        return self.locator.evaluate("el => el.options[el.selectedIndex].text")


class Checkbox(BaseElement):

    def check(self) -> None:
        self.should_be_visible()
        if not self.locator.is_checked():
            self.locator.check()

    def uncheck(self) -> None:
        self.should_be_visible()
        if self.locator.is_checked():
            self.locator.uncheck()

    def is_checked(self):
        return self.locator.is_checked()


class Link(ClickableElement):

    def href(self):
        return self.locator.get_attribute("href")
