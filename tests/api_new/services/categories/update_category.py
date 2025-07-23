import allure
import requests

from tests.api_new.services.categories.base_category import CategoryEndpoint
from tests.api_new.services.categories.urls import url


class UpdateCategory(CategoryEndpoint):

    @allure.step("Update category by id: {category_id} with payload: {payload}")
    def update_category(self, category_id, payload):
        self.response = requests.patch(
            url=url.update_category(category_id),
            json=payload
        )

        self.response_json = self.response.json()
        self.attach_response(self.response_json)
