from http import HTTPStatus

import pytest

from tests.api.services.categories.get_all_categories import GetAllCategories
from tests.api.services.categories.get_category import GetCategory


class TestGetCategory(GetCategory, GetAllCategories):

    @pytest.mark.parametrize(
        "is_test, category_id",
        [
            ("positive", "placeholder id"),
            ("negative", "wrong id"),
            ("negative", 12345678),
        ]
    )
    def test_get_category_by_id(self, is_test, category_id):
        if category_id == "placeholder id":
            category_id = self.get_random_category_id()

        self.get_category_by_id(category_id)

        if is_test == "positive":
            assert self.check_response_is(HTTPStatus.OK)
            self.validate_category()
        else:
            assert self.check_response_is(HTTPStatus.UNPROCESSABLE_ENTITY)
