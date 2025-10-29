from .base_page import BasePage


class ButtonsPage(BasePage):
    URL = "https://demoqa.com/buttons"

    def goto(self, url=None):
        # Keeps compatibility with BasePage.goto
        super().goto(url or self.URL)

    def double_click(self):
        self.page.dblclick("#doubleClickBtn")

    def right_click(self):
        self.page.click("#rightClickBtn", button="right")

    def dynamic_click(self):
        self.page.locator('button:has-text("Click Me")').nth(2).click()

    def double_click_msg(self):
        return self.page.locator("#doubleClickMessage").inner_text()

    def right_click_msg(self):
        return self.page.locator("#rightClickMessage").inner_text()

    def dynamic_click_msg(self):
        return self.page.locator("#dynamicClickMessage").inner_text()
