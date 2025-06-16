from .base_page import BasePage

class InventoryPage(BasePage):
    URL = "https://www.saucedemo.com/inventory.html"
    CART_BUTTON = ".shopping_cart_link"
    ITEM_NAME = ".inventory_item_name"

    async def go_to_cart(self):
        await self.click(self.CART_BUTTON)

    async def get_first_item_name(self) -> str:
        return await self.get_text(self.ITEM_NAME)
