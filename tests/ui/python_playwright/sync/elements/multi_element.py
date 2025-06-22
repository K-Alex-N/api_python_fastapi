from typing import Type, List, TypeVar, Generic
from playwright.sync_api import Page, Locator

T = TypeVar("T")


class MultiElement(Generic[T]):
    def __init__(self, page: Page, selector: str, element_class: Type[T]):
        self.page = page
        self.selector = selector
        self.locator: Locator = page.locator(selector)
        self.element_class = element_class

    def all(self) -> List[T]:
        count = self.locator.count()
        return [self.element_class(self.page, f"{self.selector} >> nth={i}") for i in range(count)]

    def first(self) -> T:
        return self.element_class(self.page, f"{self.selector} >> nth=0")

    def last(self) -> T:
        return self.element_class(self.page, f"{self.selector} >> nth=last")
