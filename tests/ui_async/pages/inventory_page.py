import allure
from playwright.async_api import Page

from ..components.cart_component import CartComponent
from ..components.menu_component import MenuComponent
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
        self.menu = MenuComponent(page)
        self.cart = CartComponent(page)

    @allure.step("open inventory page")
    async def open(self) -> None:
        await self.goto(self.url)

    @allure.step("Set sort order to '{label}'")
    async def set_sort_order(self, label: str) -> None:
        await self.sort_dropdown.select_by_label(label)

    async def _get_product_titles_list(self) -> list[str]:
        with allure.step("getting product titles"):
            elements = await self.product_titles.all()
            return [await x.text() for x in elements]

    async def _get_product_prices_list(self) -> list[float]:
        with allure.step("getting product prices"):
            elements = await self.product_prices.all()
            price_list = []
            for x in elements:
                price = float((await x.text())[1::])
                price_list.append(price)
            return price_list

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
        product_prices_list = await self._get_product_prices_list()
        assert product_prices_list == sorted(product_prices_list)

    @allure.step("check if products are sorted in correct order")
    async def is_products_sorted_by_price_from_high_to_low(self) -> None:
        product_prices_list = await self._get_product_prices_list()
        assert product_prices_list == sorted(product_prices_list, reverse=True)

    @allure.step("Получаем все названия продуктов на странице")
    async def get_all_product_titles(self) -> list[str]:
        return await self._get_product_titles_list()

    @allure.step("Получаем количество продуктов на странице")
    async def get_products_count(self) -> int:
        return len(await self._get_product_titles_list())

    @allure.step("Проверить наличие меню на странице")
    async def menu_should_be_visible(self) -> None:
        assert await self.menu.is_visible(), "Меню не отображается на странице!"

    @allure.step("Проверить наличие корзины на странице")
    async def cart_should_be_visible(self) -> None:
        assert await self.cart.cart_icon.is_visible(), "Корзина не отображается на странице!"
