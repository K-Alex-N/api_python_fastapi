from playwright.async_api import Page

from .base_components import BaseComponent


class ProductComponent(BaseComponent):
    def __init__(self, page: Page, product_name: str):
        self.page = page
        self.product_locator = page.locator(f".inventory_item:has-text('{product_name}')")
        self.add_to_cart_button = self.product_locator.locator("button:has-text('Add to cart')")
        self.remove_button = self.product_locator.locator("button:has-text('Remove')")

    async def add_to_cart(self) -> None:
        await self.add_to_cart_button.click()

    async def remove_from_cart(self) -> None:
        await self.remove_button.click()

    async def is_in_cart(self) -> bool:
        return await self.remove_button.is_visible()

    async def is_components_present(self) -> bool:
        return await self.product_locator.is_visible() and (
            await self.add_to_cart_button.is_visible() or await self.remove_button.is_visible()
        )
