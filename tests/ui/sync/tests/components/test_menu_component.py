import pytest


@pytest.mark.usefixtures("inventory_page")
def test_menu_component_functionality(inventory_page):
    menu = inventory_page.menu
    assert menu.is_visible(), "Menu burger button should be visible"
    menu.open_menu()
    assert menu.is_menu_open(), "Menu panel not visible after open_menu()"
    menu.close_menu()
    assert not menu.is_menu_open(), "Menu panel still visible after close_menu()"
    assert menu.is_visible(), "Menu burger button should be visible after menu closed"
    # menu.open_menu()
    # menu.click_menu_item("Logout")
