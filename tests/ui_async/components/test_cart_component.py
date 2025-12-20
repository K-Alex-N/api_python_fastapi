import os

import pytest


@pytest.mark.asyncio
async def test_cart_component_functionality(inventory_page):
    cart = inventory_page.cart

    # Проверка, что иконка корзины видима
    assert await cart.cart_icon.is_visible(), "Cart icon should be visible"

    # Счетчик по дефолту либо пустой, либо 0
    count = await cart.get_cart_count()
    assert isinstance(count, int), "Cart counter type should be int"
    assert count >= 0, "Cart counter can't be negative"

    # Открываем корзину (асинхронно)
    await cart.open_cart()


@pytest.mark.asyncio
async def test_cart_icon_screenshot(inventory_page):
    cart = inventory_page.cart
    screenshots_dir = "screenshots"
    os.makedirs(screenshots_dir, exist_ok=True)
    # Скриншот иконки корзины
    await cart.cart_icon.screenshot(path=os.path.join(screenshots_dir, "cart_icon.png"))
    # Скриншот всей страницы (через page)
    await inventory_page.page.screenshot(
        path=os.path.join(screenshots_dir, "inventory_page_cart_icon_full.png"), full_page=True
    )
