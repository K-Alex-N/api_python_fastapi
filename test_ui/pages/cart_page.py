from .base_page import BasePage

class CartPage(BasePage):
    URL = "https://www.saucedemo.com/cart.html"
    CART_ITEMS = ".cart_item"

    async def get_cart_items_count(self) -> int:
        return await self.page.locator(self.CART_ITEMS).count()
