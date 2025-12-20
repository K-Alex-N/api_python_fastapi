from playwright.async_api import Page

from .base_components import BaseComponent


class MenuComponent(BaseComponent):
    def __init__(self, page: Page):
        self.page = page
        self.burger_button = page.locator("#react-burger-menu-btn")
        self.close_button = page.locator("#react-burger-cross-btn")
        self.menu_panel = page.locator("nav.bm-item-list")
        self.menu_items = self.menu_panel.locator("a.bm-item-list")

    async def open_menu(self) -> None:
        await self.burger_button.click()

    async def close_menu(self) -> None:
        await self.close_button.click()

    async def is_menu_open(self) -> bool:
        return await self.menu_panel.is_visible()

    async def is_visible(self) -> bool:
        return await self.burger_button.is_visible()

    async def is_components_present(self) -> bool:
        return all(
            [
                await self.burger_button.is_visible(),
                await self.close_button.is_visible(),
                await self.menu_panel.is_visible(),
            ]
        )

    async def click_menu_item(self, item_text: str) -> None:
        await self.menu_panel.locator(f'a:has-text("{item_text}")').click()
