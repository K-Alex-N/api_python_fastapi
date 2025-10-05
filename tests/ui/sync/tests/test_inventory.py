import allure
import pytest

from ..pages.inventory_page import InventoryPage


@allure.epic("UI")
@allure.feature("Sync")
@allure.story("Inventory")
class TestInventory:
    def test_products_sort_by_name_from_a_to_z(self, inventory_page: InventoryPage) -> None:
        # by default sort order is 'Name (A to Z)'
        inventory_page.is_products_sorted_by_name_from_a_to_z()

    def test_products_sort_by_name_from_z_to_a(self, inventory_page: InventoryPage) -> None:
        inventory_page.set_sort_order("Name (Z to A)")
        inventory_page.is_products_sorted_by_name_from_z_to_a()

    def test_products_sort_by_price_from_low_to_high(self, inventory_page: InventoryPage) -> None:
        inventory_page.set_sort_order("Price (low to high)")
        inventory_page.is_products_sorted_by_price_from_low_to_high()

    def test_products_sort_by_price_from_high_to_low(self, inventory_page: InventoryPage) -> None:
        inventory_page.set_sort_order("Price (high to low)")
        inventory_page.is_products_sorted_by_price_from_high_to_low()

    @pytest.mark.xfail(reason="ошибка 42")
    def test_example_of_failed_test(self, inventory_page: InventoryPage) -> None:
        assert 1 == 2
