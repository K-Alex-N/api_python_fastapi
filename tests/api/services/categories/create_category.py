from typing import Any

import allure

from tests.api.services.categories.base_category import CategoryEndpoint
from tests.api.services.categories.urls import url


class CreateCategory(CategoryEndpoint):
    @allure.step("Create category with payload: {payload}")
    async def create_category(self, payload: dict[str, Any]) -> None:
        self.response = await self.client.post(url.create_category, json=payload)
        await self.process_response()
