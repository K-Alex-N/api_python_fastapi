from typing import List

import allure
from playwright.async_api import Page

from ..elements.element_factory import ElementFactory
from .base_page import BasePage


class InventoryPage(BasePage):

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.url = "https://www.saucedemo.com/inventory.html"
        el = ElementFactory(page)
        self.product_titles = el.text_elements(".inventory_item_name")
        self.product_prices = el.text_elements(".inventory_item_price")
        self.product_button = el.buttons(".btn_inventory")
        self.sort_dropdown = el.dropdown(".product_sort_container")
        self.cart_badge = el.text_element(".shopping_cart_badge")

    @allure.step("open inventory page")
    async def open(self) -> None:
        await self.goto(self.url)

    @allure.step("Set sort order to '{label}'")
    async def set_sort_order(self, label: str) -> None:
        await self.sort_dropdown.select_by_label(label)

    @allure.step("getting product titles")
    async def _get_product_titles_list(self) -> List[str]:
        elements = await self.product_titles.all()
        return [await x.text() for x in elements]

    @allure.step("getting product prices")
    async def _get_product_prices_list(self) -> List[float]:
        elements = await self.product_prices.all()
        prices = []
        for el in elements:
            raw = await el.text()
            prices.append(float(raw[1:]))  # убираем "$"
        return prices

    @allure.step("check if products are sorted in correct order")
    async def is_products_sorted_by_name_from_a_to_z(self) -> None:
        item_name_list = await self._get_product_titles_list()
        assert item_name_list == sorted(item_name_list)

    @allure.step("check if products are sorted in correct order")
    async def is_products_sorted_by_name_from_z_to_a(self) -> None:
        item_name_list = await self._get_product_titles_list()
        assert item_name_list == sorted(item_name_list, reverse=True)

    @allure.step("check if products are sorted in correct order")
    async def is_products_sorted_by_price_from_low_to_high(self) -> None:
        prices = await self._get_product_prices_list()
        assert prices == sorted(prices)

    @allure.step("check if products are sorted in correct order")
    async def is_products_sorted_by_price_from_high_to_low(self) -> None:
        prices = await self._get_product_prices_list()
        assert prices == sorted(prices, reverse=True)
