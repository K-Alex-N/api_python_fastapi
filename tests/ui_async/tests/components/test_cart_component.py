import pytest


@pytest.mark.asyncio
@pytest.mark.usefixtures("inventory_page")
async def test_cart_component_functionality(inventory_page):
    cart = inventory_page.cart

    # Проверка, что иконка корзины видима
    assert await cart.cart_icon.is_visible(), "Cart icon should be visible"

    # Счетчик по дефолту либо пустой, либо 0
    count = await cart.get_cart_count()
    assert isinstance(count, int), "Cart counter type should be int"
    assert count >= 0, "Cart counter can't be negative"

    # Открываем корзину (нужно проверить, ушли ли на страницу корзины)
    await cart.open_cart()
    # Здесь возможно нужна еще одна ассерция для проверки редиректа/страницы
