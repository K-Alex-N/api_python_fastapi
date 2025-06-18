import allure
from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    # Работа со страницей
    def navigate_to(self, url: str):
        with allure.step(f"Navigate to URL -> {url}"):
            self.page.goto(url)

    # def reload(self):
    #     self.page.reload()
    #
    # def back(self):
    #     self.page.go_back()

    def get_current_url(self) -> str:
        with allure.step("get current url"):
            return self.page.url

    # Работа с элементами
    def click(self, selector: str):
        with allure.step(f"Click element -> {selector}"):
            self.page.locator(selector).click()

    # def click(self, selector: str, force: bool = False):
    #     self.page.locator(selector).click(force=force)

    def fill(self, selector: str, value: str):
        with allure.step(f"Fill input -> {selector} with value: {value}"):
            self.page.locator(selector).fill(value)

    def is_visible(self, selector: str) -> bool:
        with allure.step(f"Check if element is visible -> {selector}"):
            return self.page.locator(selector).is_visible()

    # def get_text(self, selector: str):
    #     return self.page.locator(selector).text_content()
    #     return self.page.locator(selector).inner_text()
    #
    # def type_text(self, selector: str, value: str, delay_ms: int = 50):
    #     self.page.locator(selector).type(value, delay=delay_ms)
    #
    # def select_option(self, selector: str, value: str):
    #     self.page.locator(selector).select_option(value)
    #
    # def get_attribute(self, selector: str, attribute: str) -> str:
    #     return self.page.locator(selector).get_attribute(attribute)
    #
    # def is_enabled(self, selector: str) -> bool:
    #     return self.page.locator(selector).is_enabled()
    #
    # def is_checked(self, selector: str) -> bool:
    #     return self.page.locator(selector).is_checked()

    # Ожидания
    # def wait_for_element(self, selector: str, timeout: int = 5000):
    #     self.page.wait_for_selector(selector, timeout=timeout)

    def wait_for_url(self, url_part: str):
        expect(self.page).to_have_url(url_part)

    def wait_for_title(self, title: str):
        expect(self.page).to_have_title(title)

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

    def hover(self, selector: str):
        with allure.step(f"Hover over element -> {selector}"):
            self.page.locator(selector).hover()

    # def check(self, selector: str):
    #     self.page.locator(selector).check()
    #
    # def uncheck(self, selector: str):
    #     self.page.locator(selector).uncheck()
    #
    # def get_locator(self, selector: str) -> Locator:
    #     return self.page.locator(selector)
