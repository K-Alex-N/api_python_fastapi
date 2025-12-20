import random

import allure
import pytest

# Используем относительные импорты для обхода проблемы с ключевым словом 'async'
from ...components.cart_component import CartComponent
from ...components.product_component import ProductComponent
from ...pages.inventory_page import InventoryPage


@allure.epic("UI")
@allure.feature("Async")
@allure.story("Inventory")
class TestInventory:
    @pytest.mark.asyncio
    async def test_products_sort_by_name_from_a_to_z(self, inventory_page: InventoryPage):
        # by default sort order is 'Name (A to Z)'
        await inventory_page.is_products_sorted_by_name_from_a_to_z()

    @pytest.mark.asyncio
    async def test_products_sort_by_name_from_z_to_a(self, inventory_page: InventoryPage):
        await inventory_page.set_sort_order("Name (Z to A)")
        await inventory_page.is_products_sorted_by_name_from_z_to_a()

    @pytest.mark.asyncio
    async def test_products_sort_by_price_from_low_to_high(self, inventory_page: InventoryPage):
        await inventory_page.set_sort_order("Price (low to high)")
        await inventory_page.is_products_sorted_by_price_from_low_to_high()

    @pytest.mark.asyncio
    async def test_products_sort_by_price_from_high_to_low(self, inventory_page: InventoryPage):
        await inventory_page.set_sort_order("Price (high to low)")
        await inventory_page.is_products_sorted_by_price_from_high_to_low()

    @pytest.mark.xfail(reason="ошибка 42")
    @pytest.mark.asyncio
    async def test_example_of_failed_test(self):
        assert 1 == 42

    @pytest.mark.asyncio
    async def test_cart_counter(self, inventory_page: InventoryPage, page):
        """
        Проверяет, что счетчик корзины увеличивается при добавлении товаров.
        """
        await inventory_page.open()
        titles = await inventory_page.get_all_product_titles()
        assert titles, "На странице нет ни одного продукта."
        product_name = random.choice(titles)
        product = ProductComponent(page, product_name)
        cart = CartComponent(page)
        current_count = await cart.get_cart_count()
        await product.add_to_cart()
        assert await cart.get_cart_count() == current_count + 1, (
            "Cart counter did not increment after adding product."
        )

    @pytest.mark.asyncio
    async def test_cart_counter_bulk(self, inventory_page: InventoryPage, page):
        """
        Проверяет, что счетчик корзины верно считает при добавлении всех товаров на странице.
        """
        await inventory_page.open()
        titles = await inventory_page.get_all_product_titles()
        cart = CartComponent(page)
        for idx, product_name in enumerate(titles, start=1):
            product = ProductComponent(page, product_name)
            await product.add_to_cart()
            assert await cart.get_cart_count() == idx, (
                f"Should be {idx} items but got {await cart.get_cart_count()}"
            )

    # можно ли объединить проверку видисомти компонентов в один тест?
    # def test_menu_is_present(self, inventory_page: InventoryPage):
    #     inventory_page.open()
    #     inventory_page.menu_should_be_visible()

    # def test_cart_icon_is_present(self, inventory_page: InventoryPage):
    #     inventory_page.open()
    #     inventory_page.cart_should_be_visible()

    # def test_add_to_cart(self, inventory_page: InventoryPage):
    #     inventory_page.add_to_cart("Sauce Labs Backpack")
    #     inventory_page.is_in_cart("Sauce Labs Backpack")

    # def test_remove_from_cart(self, inventory_page: InventoryPage):
    #     inventory_page.remove_from_cart("Sauce Labs Backpack")
    #     inventory_page.is_not_in_cart("Sauce Labs Backpack")

    # def test_add_multiple_products_to_cart(self, inventory_page: InventoryPage):
    #     inventory_page.add_to_cart("Sauce Labs Backpack")
    #     inventory_page.add_to_cart("Sauce Labs Bike Light")
    #     inventory_page.add_to_cart("Sauce Labs Bolt T-Shirt")
    #     inventory_page.is_in_cart("Sauce Labs Backpack")
    #     inventory_page.is_in_cart("Sauce Labs Bike Light")
    #     inventory_page.is_in_cart("Sauce Labs Bolt T-Shirt")
