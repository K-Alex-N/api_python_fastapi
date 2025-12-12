from playwright.sync_api import Page


class CartComponent:
    def __init__(self, page: Page):
        self.page = page
        self.cart_icon = page.locator(".shopping_cart_link")
        self.cart_badge = self.cart_icon.locator(".shopping_cart_badge")

    def open_cart(self):
        self.cart_icon.click()

    def get_cart_count(self) -> int:
        if self.cart_badge.is_visible():
            return int(self.cart_badge.inner_text())
        return 0
