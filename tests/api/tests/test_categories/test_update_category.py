from http import HTTPStatus

import allure
import pytest

from tests.api.services.categories.get_all_categories import GetAllCategories
from tests.api.services.categories.payloads import payloads
from tests.api.services.categories.update_category import UpdateCategory


@allure.epic("API")
@allure.feature("Category")
@allure.story("UpdateCategory")
@pytest.mark.asyncio(loop_scope="session")
class TestUpdateCategory:
    @pytest.mark.parametrize(
        "payload",
        [
            payloads.category(),
            payloads.category_without_name(),
            payloads.category_without_type(),
            payloads.category_without_name_and_type(),
        ],
    )
    async def test_update_category_success(self, client, payload) -> None:
        get_all_categories = GetAllCategories(client)
        update_category = UpdateCategory(client)
        
        category_id = await get_all_categories.get_random_category_id()
        await update_category.update_category(category_id, payload)

        assert await update_category.check_response_is(HTTPStatus.OK)
        await update_category.validate_category()

    @pytest.mark.parametrize(
        "category_id, payload",
        [
            ("placeholder id", payloads.category_with_wrong_name()),
            ("placeholder id", payloads.category_with_wrong_type()),
            ("wrong id", payloads.category()),
            (12345678, payloads.category_without_name()),
        ],
    )
    async def test_update_category_fails(self, client, category_id, payload) -> None:
        get_all_categories = GetAllCategories(client)
        update_category = UpdateCategory(client)
        
        if category_id == "placeholder id":
            category_id = await get_all_categories.get_random_category_id()

        await update_category.update_category(category_id, payload)

        assert await update_category.check_response_is(HTTPStatus.UNPROCESSABLE_ENTITY)
