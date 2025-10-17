from typing import Any

import allure
import requests

from tests.api.services.categories.base_category import CategoryEndpoint
from tests.api.services.categories.urls import url


class CreateCategory(CategoryEndpoint):
    @allure.step("Create category with payload: {payload}")
    def create_category(self, payload: dict[str, Any]) -> None:
        self.response = requests.post(url=url.create_category, json=payload)
        self.process_response()
        # self.client.post(url=url.create_category, json=payload)
        # self.process_response()
