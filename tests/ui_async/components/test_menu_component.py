import os

import pytest


@pytest.mark.asyncio
async def test_menu_component_functionality(inventory_page):
    menu = inventory_page.menu
    assert await menu.is_visible(), "Menu burger button should be visible"
    await menu.open_menu()
    assert await menu.is_menu_open(), "Menu panel not visible after open_menu()"
    await menu.close_menu()
    assert not await menu.is_menu_open(), "Menu panel still visible after close_menu()"
    assert await menu.is_visible(), "Menu burger button should be visible after menu closed"


@pytest.mark.asyncio
async def test_menu_component_screenshot(inventory_page):
    menu = inventory_page.menu
    screenshots_dir = "screenshots"
    os.makedirs(screenshots_dir, exist_ok=True)
    # Скриншот бургер-кнопки
    await menu.burger_button.screenshot(
        path=os.path.join(screenshots_dir, "menu_burger_button.png")
    )
    # Скриншот всей страницы
    await inventory_page.page.screenshot(
        path=os.path.join(screenshots_dir, "inventory_page_full.png"), full_page=True
    )
