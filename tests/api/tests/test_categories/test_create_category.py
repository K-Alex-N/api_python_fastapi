from http import HTTPStatus

import allure
import pytest

from tests.api.services.categories.create_category import CreateCategory
from tests.api.services.categories.payloads import payloads


@allure.epic("API")
@allure.feature("Category")
@allure.story("CreateCategory")
@pytest.mark.asyncio(loop_scope="session")
class TestCreateCategory:
    async def test_create_category_success(self, client) -> None:
        create_category = CreateCategory(client)
        await create_category.create_category(payloads.category())

        assert await create_category.check_response_is(HTTPStatus.OK)
        await create_category.validate_category()

    @pytest.mark.parametrize(
        "payload",
        [
            payloads.category_without_name(),
            payloads.category_without_type(),
            payloads.category_with_wrong_name(),
            payloads.category_with_wrong_type(),
        ],
    )
    async def test_create_category_fails(self, client, payload) -> None:
        create_category = CreateCategory(client)
        await create_category.create_category(payload)

        assert await create_category.check_response_is(HTTPStatus.UNPROCESSABLE_ENTITY)
