from tests.ui_2_demoqa.pages.base_page import BasePage


class RadioButtonPage(BasePage):
    URL = "https://demoqa.com/radio-button"

    def goto(self, url=None):
        super().goto(self.URL)

    def select(self, value):
        self.page.locator(f'label[for="{value}"]').click()

    def get_output(self):
        return (
            self.page.locator(".text-success").inner_text()
            if self.page.locator(".text-success").count()
            else None
        )
