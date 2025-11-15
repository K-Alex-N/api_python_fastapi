from http import HTTPStatus

import allure
import pytest

from tests.api.services.categories.get_all_categories import GetAllCategories
from tests.api.services.categories.get_category import GetCategory


@allure.epic("API")
@allure.feature("Category")
@allure.story("GetCategory")
@pytest.mark.asyncio(loop_scope="session")
class TestGetCategory:
    async def test_get_category_by_id_success(self, client) -> None:
        get_all_categories = GetAllCategories(client)
        get_category = GetCategory(client)
        
        category_id = await get_all_categories.get_random_category_id()
        await get_category.get_category_by_id(category_id)

        assert await get_category.check_response_is(HTTPStatus.OK)
        await get_category.validate_category()

    @pytest.mark.parametrize(
        "category_id",
        [
            "wrong id",
            12345678,
        ],
    )
    async def test_get_category_by_id_fails(self, client, category_id) -> None:
        get_category = GetCategory(client)
        await get_category.get_category_by_id(category_id)

        # Check for any error status code (4xx or 5xx)
        assert not await get_category.check_response_is(HTTPStatus.OK)
