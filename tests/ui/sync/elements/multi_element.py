from playwright.sync_api import Page

from .base import BaseElement


class MultiElement[T: BaseElement]:
    def __init__(self, page: Page, selector: str, element_class: type[T]) -> None:
        self.page = page
        self.selector = selector
        self.locator = page.locator(selector)
        self.element_class: type[T] = element_class

    def all(self) -> list[T]:
        count = self.locator.count()
        return [
            self.element_class(self.page, f"{self.selector} >> nth={i}")
            for i in range(count)
        ]

    def first(self) -> T:
        return self.element_class(self.page, f"{self.selector} >> nth=0")

    def last(self) -> T:
        return self.element_class(self.page, f"{self.selector} >> nth=last")
