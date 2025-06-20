from .elements import *
from .multi_element import *


class ElementFactory:
    def __init__(self, page):
        self.page = page

    # single element

    def text_element(self, selector):
        return TextElement(self.page, selector)

    def text_input(self, selector):
        return TextInput(self.page, selector)

    def button(self, selector):
        return Button(self.page, selector)

    def checkbox(self, selector):
        return Checkbox(self.page, selector)

    def dropdown(self, selector):
        return Dropdown(self.page, selector)

    def link(self, selector):
        return Link(self.page, selector)

    # multi element

    def text_elements(self, selector):
        return MultiElement(self.page, selector, TextElement)

    def text_inputs(self, selector):
        return MultiElement(self.page, selector, TextInput)

    def buttons(self, selector):
        return MultiElement(self.page, selector, Button)

    def checkboxes(self, selector):
        return MultiElement(self.page, selector, Checkbox)

    def links(self, selector):
        return MultiElement(self.page, selector, Link)

    def dropdowns(self, selector):
        return MultiElement(self.page, selector, Dropdown)
