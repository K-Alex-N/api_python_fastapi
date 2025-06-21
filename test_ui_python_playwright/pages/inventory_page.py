import time

import allure

from ..elements.element_factory import ElementFactory
from .base_page import BasePage


class InventoryPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.url = "https://www.saucedemo.com/inventory.html"
        el = ElementFactory(page)
        self.product_titles = el.text_elements(".inventory_item_name")
        self.product_prices = el.text_elements(".inventory_item_price")
        self.product_button = el.buttons(".btn_inventory")
        self.sort_dropdown = el.dropdown(".product_sort_container")
        self.cart_badge = el.text_element(".shopping_cart_badge")

    @allure.step("open inventory page")
    def open(self):
        self.goto(self.url)

    @allure.step("Set sort order to '{label}'")
    def set_sort_order(self, label):
        self.sort_dropdown.select_by_label(label)

    def get_item_name_list(self):
        return [x.text() for x in self.product_titles.all()]

    @allure.step("Check order")
    def is_items_sorted_from_a_to_z(self):
        item_name_list = self.get_item_name_list()
        assert item_name_list == sorted(item_name_list)

    @allure.step("Check order")
    def is_items_sorted_from_z_to_a(self):
        item_name_list = self.get_item_name_list()
        assert item_name_list == sorted(item_name_list, reverse=True)

    def is_products_sorted_by_price_low_to_high(self):
        pass

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
