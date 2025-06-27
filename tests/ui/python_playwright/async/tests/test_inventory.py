import pytest
from ..pages.inventory_page import InventoryPage
from ..utils.allure_decorators import epic, feature


@epic("UI_async")
@feature("Inventory")
@pytest.mark.asyncio
class TestInventory:
    async def test_products_sort_by_name_from_a_to_z(self, inventory_page: InventoryPage):
        # by default sort order is 'Name (A to Z)'
        await inventory_page.is_products_sorted_by_name_from_a_to_z()

    async def test_products_sort_by_name_from_z_to_a(self, inventory_page: InventoryPage):
        await inventory_page.set_sort_order("Name (Z to A)")
        await inventory_page.is_products_sorted_by_name_from_z_to_a()

    async def test_products_sort_by_price_from_low_to_high(self, inventory_page: InventoryPage):
        await inventory_page.set_sort_order("Price (low to high)")
        await inventory_page.is_products_sorted_by_price_from_low_to_high()

    async def test_products_sort_by_price_from_high_to_low(self, inventory_page: InventoryPage):
        await inventory_page.set_sort_order("Price (high to low)")
        await inventory_page.is_products_sorted_by_price_from_high_to_low()

    async def test_example_of_failed_test(self, inventory_page: InventoryPage):
        assert "a" == "b"
