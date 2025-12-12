import random

import allure
import pytest

from ..components.cart_component import CartComponent
from ..components.product_component import ProductComponent
from ..pages.inventory_page import InventoryPage


@allure.epic("UI")
@allure.feature("Sync")
@allure.story("Inventory")
class TestInventory:
    def test_products_sort_by_name_from_a_to_z(self, inventory_page: InventoryPage):
        # by default sort order is 'Name (A to Z)'
        inventory_page.is_products_sorted_by_name_from_a_to_z()

    def test_products_sort_by_name_from_z_to_a(self, inventory_page: InventoryPage):
        inventory_page.set_sort_order("Name (Z to A)")
        inventory_page.is_products_sorted_by_name_from_z_to_a()

    def test_products_sort_by_price_from_low_to_high(self, inventory_page: InventoryPage):
        inventory_page.set_sort_order("Price (low to high)")
        inventory_page.is_products_sorted_by_price_from_low_to_high()

    def test_products_sort_by_price_from_high_to_low(self, inventory_page: InventoryPage):
        inventory_page.set_sort_order("Price (high to low)")
        inventory_page.is_products_sorted_by_price_from_high_to_low()

    @pytest.mark.xfail(reason="ошибка 42")
    def test_example_of_failed_test(self):
        assert 1 == 42

    def test_cart_counter(self, inventory_page: InventoryPage, page):
        """
        Проверяет, что счетчик корзины увеличивается при добавлении товаров.
        """
        inventory_page.open()
        titles = inventory_page.get_all_product_titles()
        assert titles, "На странице нет ни одного продукта."
        product_name = random.choice(titles)
        product = ProductComponent(page, product_name)
        cart = CartComponent(page)
        current_count = cart.get_cart_count()
        product.add_to_cart()
        assert cart.get_cart_count() == current_count + 1, (
            "Cart counter did not increment after adding product."
        )

    def test_cart_counter_bulk(self, inventory_page: InventoryPage, page):
        """
        Проверяет, что счетчик корзины верно считает при добавлении всех товаров на странице.
        """
        inventory_page.open()
        titles = inventory_page.get_all_product_titles()
        cart = CartComponent(page)
        for idx, product_name in enumerate(titles, start=1):
            ProductComponent(page, product_name).add_to_cart()
            assert cart.get_cart_count() == idx, (
                f"Should be {idx} items but got {cart.get_cart_count()}"
            )

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
