from typing import Type, List
from playwright.sync_api import Page

from .base import BaseElement


class MultiElement[T: BaseElement]:
    def __init__(self, page: Page, selector: str, element_class: Type[T]):
        self.page = page
        self.selector = selector
        self.locator = page.locator(selector)
        self.element_class: Type[T] = element_class

    def all(self) -> List[T]:
        count = self.locator.count()
        return [self.element_class(self.page, f"{self.selector} >> nth={i}") for i in range(count)]

    def first(self) -> T:
        return self.element_class(self.page, f"{self.selector} >> nth=0")

    def last(self) -> T:
        return self.element_class(self.page, f"{self.selector} >> nth=last")
