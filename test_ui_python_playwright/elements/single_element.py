import allure
from playwright.sync_api import expect

from .base import BaseElement, ClickableMixin


class TextInput(BaseElement):
    """ input field (<input type="text">) """

    def fill(self, value: str):
        with allure.step(f"Fill input {self.selector} with value: {value}"):
            self.should_be_visible()
            self.locator.fill(value)

    def clear(self):
        self.locator.clear()

    def type_text(self, selector: str, value: str, delay_ms: int = 50):
        self.page.locator(selector).type(value, delay=delay_ms)


class Button(ClickableMixin, BaseElement):
    pass


class TextElement(BaseElement):
    """ elements that have text (<div>, <span> etc) """

    def text(self) -> str:
        with allure.step("Getting inner text"):
            self.should_be_visible()
            return self.locator.inner_text()
            # return self.locator.text_content()

    def should_have_text(self, expected: str):
        with allure.step(f"Text should have {expected}"):
            self.should_be_visible()
            expect(self.locator).to_have_text(expected)


class Dropdown(BaseElement):
# мб его переназвать в SelectElement ??? и select_option() соответственнно

    def select_by_value(self, value):
        self.should_be_visible()
        self.locator.select_option(value=value)

    def select_by_label(self, label):
        self.should_be_visible()
        self.locator.select_option(label=label)

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

# def select_option(self, selector: str, value: str):
#     self.page.locator(selector).select_option(value)
#
# def get_attribute(self, selector: str, attribute: str) -> str:
#     return self.page.locator(selector).get_attribute(attribute)
#

# Ожидания
# def wait_for_element(self, selector: str, timeout: int = 5000):
#     self.page.wait_for_selector(selector, timeout=timeout)

# def wait_until_hidden(self, selector: str):
#     self.page.locator(selector).wait_for(state="hidden")

# Утилиты
# def scroll_into_view(self, selector: str):
#     self.page.locator(selector).scroll_into_view_if_needed()
#
# def take_screenshot(self, path: str):
#     self.page.screenshot(path=path)
#
# def press_key(self, selector: str, key: str):
#     self.page.locator(selector).press(key)

# def hover(self, selector: str):
#     with allure.step(f"Hover over element -> {selector}"):
#         self.page.locator(selector).hover()
