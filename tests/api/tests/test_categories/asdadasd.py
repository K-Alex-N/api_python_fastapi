from http import HTTPStatus

import allure
import pytest

from app.api.categories.models import Category
from tests.api.services.categories.create_category import CreateCategory
from tests.api.services.categories.payloads import payloads


@allure.epic("API-DB")
@allure.feature("Category")
@allure.story("CreateCategory")
class TestCreateCategory(CreateCategory):
    @pytest.mark.asyncio
    async def test_db(self) -> None:
        category_payload = payloads.category()
        self.create_category(category_payload)

        assert self.check_response_is(HTTPStatus.OK)
        self.validate_category()

        # ✅ Просто await без создания нового event loop
        found = await Category.find_one(
            {"name": category_payload["name"], "type": category_payload["type"]}
        )

        assert found is not None, (
            f"Category was not found in MongoDB: {category_payload}"
        )
        assert found.name == category_payload["name"]
        assert found.type == category_payload["type"]
