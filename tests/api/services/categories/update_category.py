import allure

from tests.api.services.categories.base_category import CategoryEndpoint
from tests.api.services.categories.urls import url


class UpdateCategory(CategoryEndpoint):
    @allure.step("Update category with id: {category_id}")
    async def update_category(self, category_id, payload) -> None:
        self.response = await self.client.patch(url=url.update_category(category_id), json=payload)
        await self.process_response()
