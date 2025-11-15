import allure

from tests.api.services.categories.base_category import CategoryEndpoint
from tests.api.services.categories.get_category import GetCategory
from tests.api.services.categories.urls import url


class DeleteCategory(CategoryEndpoint):
    @allure.step("Delete category with id: {category_id}")
    async def delete_category(self, category_id) -> None:
        self.response = await self.client.delete(url=url.delete_category(category_id))
        await self.process_response()

    @staticmethod
    @allure.step("Check if category with id {category_id} deleted")
    async def is_category_deleted(category_id) -> bool:
        get_category = GetCategory()
        await get_category.get_category_by_id(category_id)
        return True if not get_category.response else False
