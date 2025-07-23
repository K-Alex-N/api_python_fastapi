import allure
import requests

from tests.api_new.services.categories.base_category import CategoryEndpoint
from tests.api_new.services.categories.urls import url
from tests.api_new.services.categories.get_category import GetCategory


class DeleteCategory(CategoryEndpoint):

    @allure.step("Delete category by id: {category_id}")
    def delete_category(self, category_id):
        self.response = requests.delete(
            url=url.delete_category(category_id)
        )
        self.response_json = self.response.json()
        self.attach_response(self.response_json)

    @staticmethod
    @allure.step("Check if category with id {category_id} deleted")
    def is_category_deleted(category_id):
        get_endpoint = GetCategory()
        response = get_endpoint.get_category_by_id(category_id)
        return True if not response else False
