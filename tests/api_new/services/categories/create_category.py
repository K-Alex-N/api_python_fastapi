import allure
import requests

from tests.api_new.services.categories.base_category import CategoryEndpoint
from tests.api_new.services.categories.urls import url


class CreateCategory(CategoryEndpoint):

    @allure.step("Create category with payload: {payload}")
    def create_category(self, payload):
        self.response = requests.post(
            url=url.create_category,
            json=payload
        )
        self.response_json = self.response.json()
        self.attach_response(self.response_json)

        # self._process_response()
