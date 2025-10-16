from playwright.sync_api import Page

from .multi_element import MultiElement
from .single_element import Button, Checkbox, Dropdown, Link, TextElement, TextInput


class ElementFactory:
    def __init__(self, page: Page) -> None:
        self.page = page

    # single element

    def text_element(self, selector: str) -> TextElement:
        return TextElement(self.page, selector)

    def text_input(self, selector: str) -> TextInput:
        return TextInput(self.page, selector)

    def button(self, selector: str) -> Button:
        return Button(self.page, selector)

    def checkbox(self, selector: str) -> Checkbox:
        return Checkbox(self.page, selector)

    def dropdown(self, selector: str) -> Dropdown:
        return Dropdown(self.page, selector)

    def link(self, selector: str) -> Link:
        return Link(self.page, selector)

    # multi element

    def text_elements(self, selector: str) -> MultiElement[TextElement]:
        return MultiElement(self.page, selector, TextElement)

    def text_inputs(self, selector: str) -> MultiElement[TextInput]:
        return MultiElement(self.page, selector, TextInput)

    def buttons(self, selector: str) -> MultiElement[Button]:
        return MultiElement(self.page, selector, Button)

    def checkboxes(self, selector: str) -> MultiElement[Checkbox]:
        return MultiElement(self.page, selector, Checkbox)

    def links(self, selector: str) -> MultiElement[Link]:
        return MultiElement(self.page, selector, Link)

    def dropdowns(self, selector: str) -> MultiElement[Dropdown]:
        return MultiElement(self.page, selector, Dropdown)
