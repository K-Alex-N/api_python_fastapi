from http import HTTPStatus

import allure
import pytest

from tests.api.services.categories.get_all_categories import GetAllCategories
from tests.api.services.categories.payloads import payloads
from tests.api.services.categories.update_category import UpdateCategory


@allure.epic("API")
@allure.feature("Category")
@allure.story("UpdateCategory")
class TestUpdateCategory(UpdateCategory, GetAllCategories):
    @pytest.mark.parametrize(
        "payload",
        [
            payloads.category(),
            payloads.category_without_name(),
            payloads.category_without_type(),
            payloads.category_without_name_and_type(),
        ],
    )
    def test_update_category_success(self, payload) -> None:
        category_id = self.get_random_category_id()
        self.update_category(category_id, payload)

        assert self.check_response_is(HTTPStatus.OK)
        self.validate_category()

    @pytest.mark.parametrize(
        "category_id, payload",
        [
            ("placeholder id", payloads.category_with_wrong_name()),
            ("placeholder id", payloads.category_with_wrong_type()),
            ("wrong id", payloads.category()),
            (12345678, payloads.category_without_name()),
        ],
    )
    def test_update_category_fails(self, category_id, payload) -> None:
        if category_id == "placeholder id":
            category_id = self.get_random_category_id()

        self.update_category(category_id, payload)

        assert self.check_response_is(HTTPStatus.UNPROCESSABLE_ENTITY)
