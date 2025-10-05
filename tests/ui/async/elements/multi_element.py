from typing import Generic, List, Type, TypeVar

from playwright.async_api import Page

from .base import BaseElement

T = TypeVar("T", bound=BaseElement)


class MultiElement(Generic[T]):
    def __init__(self, page: Page, selector: str, element_class: Type[T]) -> None:
        self.page = page
        self.selector = selector
        self.locator = page.locator(selector)
        self.element_class: Type[T] = element_class

    async def all(self) -> List[T]:
        count = await self.locator.count()
        return [self.element_class(self.page, f"{self.selector} >> nth={i}") for i in range(count)]

    async def first(self) -> T:
        return self.element_class(self.page, f"{self.selector} >> nth=0")

    async def last(self) -> T:
        return self.element_class(self.page, f"{self.selector} >> nth=last")
