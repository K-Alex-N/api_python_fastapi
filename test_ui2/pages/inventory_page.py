from .elements import *
from .base_page import BasePage


class InventoryPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.url = "https://www.saucedemo.com/inventory.html"
        self.item_name = Text(page, ".inventory_item_name")
        self.item_price = Text(page, ".inventory_item_price")
        self.item_button = Button(page, ".btn_inventory")
        self.sort_dropdown = Dropdown(page, ".product_sort_container")
        self.cart_badge = Text(page, ".shopping_cart_badge")

    def open(self):
        self.goto(self.url)

    def is_items_sorted_from_A_to_Z(self):
        pass


    # def login(self, username: str, password: str):
    #     self.username_input.fill(username)
    #     self.password_input.fill(password)
    #     self.login_button.click()
