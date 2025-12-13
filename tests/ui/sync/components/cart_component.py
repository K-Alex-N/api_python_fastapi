from playwright.sync_api import Page

from .base_components import BaseComponent


class CartComponent(BaseComponent):
    def __init__(self, page: Page):
        self.page = page
        self.cart_icon = page.locator(".shopping_cart_link")
        self.cart_badge = self.cart_icon.locator(".shopping_cart_badge")

    def open_cart(self) -> None:
        self.cart_icon.click()

    def get_cart_count(self) -> int:
        if self.cart_badge.is_visible():
            return int(self.cart_badge.inner_text())
        return 0

    def is_components_present(self) -> bool:
        # cart_icon должен быть всегда, badge опционально
        return self.cart_icon.is_visible()
