from typing import Any

import allure

from tests.api.services.categories.base_category import CategoryEndpoint
from tests.api.services.categories.urls import url


class CreateCategory(CategoryEndpoint):
    @allure.step("Create category with payload: {payload}")
    def create_category(self, payload: dict[str, Any]) -> None:
        self.response = self.client.post(url.create_category, json=payload)
        self.process_response()
