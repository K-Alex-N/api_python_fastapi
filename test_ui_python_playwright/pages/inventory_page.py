from test_ui_python_playwright.elements.elements import *
from .base_page import BasePage


class InventoryPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.url = "https://www.saucedemo.com/inventory.html"
        self.item_name = TextElement(page, ".inventory_item_name")
        self.item_price = TextElement(page, ".inventory_item_price")
        self.item_button = Button(page, ".btn_inventory")
        self.sort_dropdown = Dropdown(page, ".product_sort_container")
        self.cart_badge = TextElement(page, ".shopping_cart_badge")

    @allure.step("open inventory page")
    def open(self):
        self.goto(self.url)

    def is_items_sorted_from_A_to_Z(self):
        # item_names = self.item_name.all()
        # item_names_text = []
        # for item in item_names:
        #     item = TextElement(it)
        #     item_names_text.append(item)
        pass



        # items = self.page.locator(".inventory_item_name").all()
        # for item in items:
        #     print(item.all_inner_texts())

        # items_2 = self.item_name.inner_text()
        # print(items_2)