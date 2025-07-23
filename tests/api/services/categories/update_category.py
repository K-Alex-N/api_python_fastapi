import allure
import requests

from tests.api.services.categories.base_category import CategoryEndpoint
from tests.api.services.categories.urls import url


class UpdateCategory(CategoryEndpoint):

    @allure.step("Update category by id: {category_id} with payload: {payload}")
    def update_category(self, category_id, payload):
        self.response = requests.patch(
            url=url.update_category(category_id),
            json=payload
        )
        self._process_response()
