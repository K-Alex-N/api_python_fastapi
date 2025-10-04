import allure
from playwright.async_api import expect

from .base import BaseElement, ClickableElement


class TextInput(BaseElement):
    """input field (<input type="text">)"""

    async def fill(self, value: str) -> None:
        with allure.step(f"Fill input {self.selector} with value: {value}"):
            await self.should_be_visible()
            await self.locator.fill(value)

    async def clear(self) -> None:
        await self.locator.clear()

    async def type_text(self, selector: str, value: str, delay_ms: int = 50) -> None:
        await self.page.locator(selector).type(value, delay=delay_ms)


class Button(ClickableElement):
    pass


class TextElement(BaseElement):
    """elements that have text (<div>, <span> etc)"""

    async def text(self) -> str:
        with allure.step("Getting inner text"):
            await self.should_be_visible()
            return await self.locator.inner_text()

    async def should_have_text(self, expected: str) -> None:
        with allure.step(f"Text should have {expected}"):
            await self.should_be_visible()
            await expect(self.locator).to_have_text(expected)


class Dropdown(BaseElement):
    # возможно переименовать в SelectElement

    async def select_by_value(self, value: str) -> None:
        await self.should_be_visible()
        await self.locator.select_option(value=value)

    async def select_by_label(self, label: str) -> None:
        await self.should_be_visible()
        await self.locator.select_option(label=label)

    async def get_selected_option_label(self) -> str:
        return await self.locator.evaluate("el => el.options[el.selectedIndex].text")


class Checkbox(BaseElement):

    async def check(self) -> None:
        await self.should_be_visible()
        if not await self.locator.is_checked():
            await self.locator.check()

    async def uncheck(self) -> None:
        await self.should_be_visible()
        if await self.locator.is_checked():
            await self.locator.uncheck()

    async def is_checked(self) -> bool:
        return await self.locator.is_checked()


class Link(ClickableElement):

    async def href(self) -> str:
        return await self.locator.get_attribute("href")
