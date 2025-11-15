from http import HTTPStatus

import allure
import pytest

from tests.api.services.categories.delete_category import DeleteCategory
from tests.api.services.categories.get_all_categories import GetAllCategories


@allure.epic("API")
@allure.feature("Category")
@allure.story("DeleteCategory")
@pytest.mark.asyncio(loop_scope="session")
class TestDeleteCategory:
    @pytest.mark.parametrize(
        "is_test, category_id",
        [
            ("-negative", "wrong id"),
        ],
    )
    async def test_delete_category(self, client, is_test, category_id) -> None:
        get_all_categories = GetAllCategories(client)
        delete_category = DeleteCategory(client)

        if category_id == "placeholder id":
            category_id = await get_all_categories.get_random_category_id()

        await delete_category.delete_category(category_id)

        if is_test == "positive":
            assert await delete_category.check_response_is(HTTPStatus.OK)
            assert await delete_category.is_category_deleted(category_id)
        else:
            assert await delete_category.check_response_is(
                HTTPStatus.UNPROCESSABLE_ENTITY
            )
