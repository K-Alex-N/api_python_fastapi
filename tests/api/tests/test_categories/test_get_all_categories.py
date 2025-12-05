from http import HTTPStatus

import allure
import pytest

from tests.api.services.categories.get_all_categories import GetAllCategories


@allure.epic("API")
@allure.feature("Category")
@allure.story("GetAllCategories")
@pytest.mark.asyncio(loop_scope="session")
class TestGetAllCategories:
    async def test_get_all_categories(self, client):
        get_all_categories = GetAllCategories(client)
        await get_all_categories.get_all_categories()

        assert await get_all_categories.check_response_is(HTTPStatus.OK)
        await get_all_categories.validate_list_of_categories()
