from playwright.sync_api import Page

from .base_components import BaseComponent


class MenuComponent(BaseComponent):
    def __init__(self, page: Page):
        self.page = page
        self.burger_button = page.locator("#react-burger-menu-btn")
        self.close_button = page.locator("#react-burger-cross-btn")
        self.menu_panel = page.locator("nav.bm-item-list")
        self.menu_items = self.menu_panel.locator("a.bm-item-list")

    def open_menu(self) -> None:
        self.burger_button.click()

    def close_menu(self) -> None:
        self.close_button.click()

    def is_menu_open(self) -> bool:
        return self.menu_panel.is_visible()

    def is_components_present(self) -> bool:
        return all(
            [
                self.burger_button.is_visible(),
                self.close_button.is_visible(),
                self.menu_panel.is_visible(),
            ]
        )

    def click_menu_item(self, item_text: str) -> None:
        self.menu_panel.locator(f'a:has-text("{item_text}")').click()
