import pytest


@pytest.mark.asyncio
@pytest.mark.usefixtures("inventory_page")
async def test_menu_component_functionality(inventory_page):
    menu = inventory_page.menu
    assert await menu.is_visible(), "Menu burger button should be visible"
    await menu.open_menu()
    assert await menu.is_menu_open(), "Menu panel not visible after open_menu()"
    await menu.close_menu()
    assert not await menu.is_menu_open(), "Menu panel still visible after close_menu()"
    assert await menu.is_visible(), "Menu burger button should be visible after menu closed"
    # await menu.open_menu()
    # await menu.click_menu_item("Logout")
