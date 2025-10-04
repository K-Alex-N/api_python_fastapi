import allure
import requests

from tests.api.services.categories.base_category import CategoryEndpoint
from tests.api.services.categories.urls import url


class GetCategory(CategoryEndpoint):

    @allure.step("Get category by id: {category_id}")
    def get_category_by_id(self, category_id) -> None:
        self.response = requests.get(url=url.get_category_by_id(category_id))
        self.process_response()
