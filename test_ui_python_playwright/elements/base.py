import allure
from playwright.sync_api import expect, Page, Locator

class BaseElement:
    def __init__(self, page: Page, selector: str, description: str = None):
        self.page = page
        self.selector = selector
        self.locator: Locator = page.locator(selector)
        self.description = description if description else f"элемент с селектором '{selector}'"
        # Playwright Locator уже может представлять один или несколько элементов.
        # Мы будем работать с ним как с коллекцией, но по умолчанию действовать на .first

    @allure.step("expect to be visible")
    def should_be_visible(self):
        expect(self.locator).to_be_visible()

    @allure.step("expect to be enabled")
    def should_be_enabled(self):
        expect(self.locator).to_be_enabled()

    # def get_text(self) -> str:
    #     self.wait_for_visible() # Убедимся, что элемент виден, прежде чем получить текст
    #     return self.locator.text_content()

    #
    # methods for work with many element (found with one locator)
    #

    # def count(self) -> int:
    #     """the number of elements found"""
    #     return self.locator.count()
    #
    # def get_nth(self, index: int) -> 'BaseElement':
    #     """Возвращает новый экземпляр BaseElement для конкретного элемента по индексу."""
    #     if index < 0 or index >= self.count():
    #         raise IndexError(
    #             f"Индекс {index} выходит за пределы диапазона для {self.description} (найдено {self.count()} элементов).")
    #     # Возвращаем новый экземпляр BaseElement для конкретного элемента
    #     # Это позволяет выполнять действия над конкретным элементом, а не над первым
    #     return BaseElement(self.page, self.selector + f":nth-of-type({index + 1})",
    #                        f"{self.description} под индексом {index}")
    #     # Или, более прямолинейно и правильно, использовать .nth()
    #     # return BaseElement(self.page, None, f"{self.description} под индексом {index}")._with_locator(self.locator.nth(index))
    #
    # # Вспомогательный метод для создания нового элемента с конкретным локатором (без селектора)
    # def _with_locator(self, locator: Locator):
    #     new_element = BaseElement(self.page, self.selector)  # Передаем оригинальный селектор для идентификации
    #     new_element.locator = locator
    #     return new_element
    #
    # def all(self) -> list['BaseElement']:
    #     """Возвращает список объектов BaseElement для всех найденных элементов."""
    #     elements = []
    #     for i in range(self.count()):
    #         elements.append(self._with_locator(self.locator.nth(i)))
    #     return elements
    #
    # # Метод для итерации по найденным элементам (Pythonic way)
    # def __getitem__(self, index: int) -> 'BaseElement':
    #     return self._with_locator(self.locator.nth(index))
    #
    # def __len__(self) -> int:
    #     return self.count()


# Mixins


class ClickableMixin:

    def click(self):
        """Click on element. If more than 1 element then error will be raised"""
        with allure.step(f"Click {self.description}"):
            self.should_be_visible()
            self.should_be_enabled()
            self.locator.click()

    def click_first(self):
        """Clicks on the first element found."""
        with allure.step(f"Click element {self.selector}"):
            self.should_be_visible()
            self.should_be_enabled()
            self.locator.first.click()
