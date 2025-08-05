import allure
import pytest
from ..pages.inventory_page import InventoryPage

@allure.epic("UI")
@allure.feature("Async")
@allure.story("Inventory")
@pytest.mark.asyncio
class TestInventory:
    async def test_products_sort_by_name_from_a_to_z_async(self, inventory_page: InventoryPage):
        # by default sort order is 'Name (A to Z)'
        await inventory_page.is_products_sorted_by_name_from_a_to_z()

    async def test_products_sort_by_name_from_z_to_a_async(self, inventory_page: InventoryPage):
        await inventory_page.set_sort_order("Name (Z to A)")
        await inventory_page.is_products_sorted_by_name_from_z_to_a()

    async def test_products_sort_by_price_from_low_to_high_async(self, inventory_page: InventoryPage):
        await inventory_page.set_sort_order("Price (low to high)")
        await inventory_page.is_products_sorted_by_price_from_low_to_high()

    async def test_products_sort_by_price_from_high_to_low_async(self, inventory_page: InventoryPage):
        await inventory_page.set_sort_order("Price (high to low)")
        await inventory_page.is_products_sorted_by_price_from_high_to_low()

    async def test_example_of_failed_test_async(self, inventory_page: InventoryPage):
        assert "a" == "b"
