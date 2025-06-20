class MultiElement:
    def __init__(self, page, selector, element_class):
        self.page = page
        self.selector = selector
        self.locator = page.locator(selector)
        self.element_class = element_class

    def all(self):
        count = self.locator.count()
        return [self.element_class(self.page, f"{self.selector} >> nth={i}") for i in range(count)]

    def first(self):
        return self.element_class(self.page, f"{self.selector} >> nth=0")

    def last(self):
        count = self.locator.count()
        return self.element_class(self.page, f"{self.selector} >> nth={count - 1}")
