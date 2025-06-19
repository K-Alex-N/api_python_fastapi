from .base_page import BasePage






class InventoryPage(BasePage):
    INVENTORY_ITEM_NAME = ".inventory_item_name"


    def __init__(self, page):
        super().__init__(page)
        self.url = "https://www.saucedemo.com/inventory.html"
        # self.username_input = page.locator("#user-name")
        # self.password_input = page.locator("#password")
        # self.login_button = page.locator("#login-button")
        # self.error_message = page.locator("[data-test='error']")

    def open(self):
        self.navigate_to(self.url)


    def is_items_sorted_from_A_to_Z(self):
        pass



    # URL = "https://www.saucedemo.com/"
    # USERNAME_INPUT = "#user-name"
    # PASSWORD_INPUT = "#password"
    # LOGIN_BUTTON = "#login-button"
    # ERROR_MESSAGE = "[data-test='error']"

    # def login(self, username: str, password: str):
    #     self.username_input.fill(username)
    #     self.password_input.fill(password)
    #     self.login_button.click()

