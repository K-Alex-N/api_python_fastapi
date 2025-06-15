from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str):
        self.page.goto(url)

    def get_current_url(self) -> str:
        return self.page.url

    def get_text(self, locator: str) -> str:
        return self.page.locator(locator).inner_text()

    def click(self, locator: str):
        self.page.locator(locator).click()

    def fill(self, locator: str, text: str):
        self.page.locator(locator).fill(text)
