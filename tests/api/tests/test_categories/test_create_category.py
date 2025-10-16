from http import HTTPStatus

import allure
import pytest

from tests.api.services.categories.create_category import CreateCategory
from tests.api.services.categories.payloads import payloads


@allure.epic("API")
@allure.feature("Category")
@allure.story("CreateCategory")
class TestCreateCategory(CreateCategory):
    def test_create_category_success(self) -> None:
        self.create_category(payloads.category())

        assert self.check_response_is(HTTPStatus.OK)
        self.validate_category()

    @pytest.mark.parametrize(
        "payload",
        [
            payloads.category_without_name(),
            payloads.category_without_type(),
            payloads.category_with_wrong_name(),
            payloads.category_with_wrong_type(),
        ],
    )
    def test_create_category_fails(self, payload) -> None:
        self.create_category(payload)

        assert self.check_response_is(HTTPStatus.UNPROCESSABLE_ENTITY)
