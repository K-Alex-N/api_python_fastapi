import os

import pytest


@pytest.mark.usefixtures("inventory_page")
def test_cart_component_functionality(inventory_page):
    cart = inventory_page.cart
    assert cart.cart_icon.is_visible(), "Cart icon should be visible"
    count = cart.get_cart_count()
    assert isinstance(count, int), "Cart counter type should be int"
    assert count >= 0, "Cart counter can't be negative"
    cart.open_cart()


def test_cart_icon_screenshot(inventory_page):
    cart = inventory_page.cart
    screenshots_dir = "screenshots"
    os.makedirs(screenshots_dir, exist_ok=True)
    # Скриншот иконки корзины
    cart.cart_icon.screenshot(path=os.path.join(screenshots_dir, "cart_icon.png"))
    # Скриншот всей страницы (через page)
    inventory_page.page.screenshot(
        path=os.path.join(screenshots_dir, "inventory_page_cart_icon_full.png"), full_page=True
    )
