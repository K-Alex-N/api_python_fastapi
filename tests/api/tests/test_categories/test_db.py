from http import HTTPStatus

import allure
import pytest

from app.api.categories.models import Category
from tests.api.services.categories.create_category import CreateCategory
from tests.api.services.categories.payloads import payloads


@allure.epic("API-DB")
@allure.feature("Category")
@allure.story("CreateCategory")
@pytest.mark.asyncio(loop_scope="session")
class TestCreateCategory:
    async def test_db(self, client):
        create_category = CreateCategory(client)
        payload = payloads.category()

        # create a category
        await create_category.create_category(payload)

        # check response
        assert await create_category.check_response_is(HTTPStatus.OK)
        await create_category.validate_category()

        # check db
        db_data = await Category.find_one(
            {
                "name": payload["name"],
                "type": payload["type"],
            }
        )
        assert db_data is not None, f"Category not found: {payload}"
