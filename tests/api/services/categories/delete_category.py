import allure
import requests

from tests.api.services.categories.base_category import CategoryEndpoint
from tests.api.services.categories.get_category import GetCategory
from tests.api.services.categories.urls import url


class DeleteCategory(CategoryEndpoint):
    @allure.step("Delete category by id: {category_id}")
    def delete_category(self, category_id) -> None:
        self.response = requests.delete(url=url.delete_category(category_id))
        self.process_response()

    @staticmethod
    @allure.step("Check if category with id {category_id} deleted")
    def is_category_deleted(category_id) -> bool:
        response = GetCategory().get_category_by_id(category_id)
        return True if not response else False
