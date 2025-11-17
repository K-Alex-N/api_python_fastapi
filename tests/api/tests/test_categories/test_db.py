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
        category_payload = payloads.category()
        await create_category.create_category(category_payload)

        assert await create_category.check_response_is(HTTPStatus.OK)
        await create_category.validate_category()

        db_data = await Category.find_one(
            {
                "name": category_payload["name"],
                "type": category_payload["type"],
            }
        )

        assert db_data is not None, f"Category not found: {category_payload}"
        assert db_data.name == category_payload["name"]
        assert db_data.type == category_payload["type"]
