from playwright.sync_api import Page


class ProductComponent:
    def __init__(self, page: Page, product_name: str):
        self.page = page
        self.product_locator = page.locator(f".inventory_item:has-text('{product_name}')")
        self.add_to_cart_button = self.product_locator.locator("button:has-text('Add to cart')")
        self.remove_button = self.product_locator.locator("button:has-text('Remove')")

    def add_to_cart(self):
        self.add_to_cart_button.click()

    def remove_from_cart(self):
        self.remove_button.click()

    def is_in_cart(self) -> bool:
        return self.remove_button.is_visible()
