import allure

from tests.api.services.categories.base_category import CategoryEndpoint
from tests.api.services.categories.urls import url


class GetCategory(CategoryEndpoint):
    @allure.step("Get category by id: {category_id}")
    async def get_category_by_id(self, category_id) -> None:
        self.response = await self.client.get(url=url.get_category_by_id(category_id))
        await self.process_response()
