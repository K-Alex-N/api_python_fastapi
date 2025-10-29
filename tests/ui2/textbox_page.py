from .base_page import BasePage


class TextBoxPage(BasePage):
    URL = "https://demoqa.com/text-box"

    def goto(self, url=None):
        super().goto(self.URL)

    def fill_form(self, name, email, current_address, permanent_address):
        self.page.locator("#userName").fill(name)
        self.page.locator("#userEmail").fill(email)
        self.page.locator("#currentAddress").fill(current_address)
        self.page.locator("#permanentAddress").fill(permanent_address)

    def submit(self):
        self.page.locator("#submit").click()

    def get_output_text(self):
        return self.page.locator("#output").inner_text()
