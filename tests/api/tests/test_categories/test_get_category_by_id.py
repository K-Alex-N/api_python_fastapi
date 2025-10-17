from http import HTTPStatus

import allure
import pytest

from tests.api.services.categories.get_all_categories import GetAllCategories
from tests.api.services.categories.get_category import GetCategory


@allure.epic("API")
@allure.feature("Category")
@allure.story("GetCategory")
class TestGetCategory(GetCategory, GetAllCategories):
    def test_get_category_by_id_success(self) -> None:
        category_id = self.get_random_category_id()
        self.get_category_by_id(category_id)

        assert self.check_response_is(HTTPStatus.OK)
        self.validate_category()

    @pytest.mark.parametrize(
        "category_id",
        [
            "wrong id",
            12345678,
        ],
    )
    def test_get_category_by_id_fails(self, category_id) -> None:
        self.get_category_by_id(category_id)

        assert self.check_response_is(HTTPStatus.UNPROCESSABLE_ENTITY)
