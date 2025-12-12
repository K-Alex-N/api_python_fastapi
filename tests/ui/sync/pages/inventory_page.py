import allure
from playwright.sync_api import Page

from ..elements.element_factory import ElementFactory
from .base_page import BasePage


class InventoryPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.url = self.base_url + "/inventory.html"
        el = ElementFactory(page)
        self.product_titles = el.text_elements(".inventory_item_name")
        self.product_prices = el.text_elements(".inventory_item_price")
        self.product_button = el.buttons(".btn_inventory")
        self.sort_dropdown = el.dropdown(".product_sort_container")
        self.cart_badge = el.text_element(".shopping_cart_badge")

    @allure.step("open inventory page")
    def open(self) -> None:
        self.goto(self.url)

    @allure.step("Set sort order to '{label}'")
    def set_sort_order(self, label: str) -> None:
        self.sort_dropdown.select_by_label(label)

    @allure.step("getting product titles")
    def _get_product_titles_list(self) -> list[str]:
        return [x.text() for x in self.product_titles.all()]

    @allure.step("getting product prices")
    def _get_product_prices_list(self) -> list[float]:
        price_list = []
        for x in self.product_prices.all():
            price = float(x.text()[1::])
            price_list.append(price)
        return price_list

    @allure.step("check if products are sorted in correct order")
    def is_products_sorted_by_name_from_a_to_z(self) -> None:
        item_name_list = self._get_product_titles_list()
        assert item_name_list == sorted(item_name_list)

    @allure.step("check if products are sorted in correct order")
    def is_products_sorted_by_name_from_z_to_a(self) -> None:
        item_name_list = self._get_product_titles_list()
        assert item_name_list == sorted(item_name_list, reverse=True)

    @allure.step("check if products are sorted in correct order")
    def is_products_sorted_by_price_from_low_to_high(self) -> None:
        product_prices_list = self._get_product_prices_list()
        assert product_prices_list == sorted(product_prices_list)

    @allure.step("check if products are sorted in correct order")
    def is_products_sorted_by_price_from_high_to_low(self) -> None:
        product_prices_list = self._get_product_prices_list()
        assert product_prices_list == sorted(product_prices_list, reverse=True)

    @allure.step("Получаем все названия продуктов на странице")
    def get_all_product_titles(self) -> list[str]:
        return self._get_product_titles_list()

    @allure.step("Получаем количество продуктов на странице")
    def get_products_count(self) -> int:
        return len(self._get_product_titles_list())
