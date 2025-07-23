from http import HTTPStatus

import pytest

from tests.api.services.categories.get_all_categories import GetAllCategories
from tests.api.services.categories.payloads import payloads
from tests.api.services.categories.update_category import UpdateCategory


class TestUpdateCategory(UpdateCategory, GetAllCategories):

    @pytest.mark.parametrize(
        "is_test, category_id, payload",
        [
            ("positive", "placeholder id", payloads.category()),
            ("positive", "placeholder id", payloads.category_without_name()),
            ("positive", "placeholder id", payloads.category_without_type()),
            ("positive", "placeholder id", payloads.category_without_name_and_type()),
            ("negative", "placeholder id", payloads.category_with_wrong_name()),
            ("negative", "placeholder id", payloads.category_with_wrong_type()),
            ("negative", "wrong id", payloads.category()),
            ("negative", 12345678, payloads.category_without_name()),
        ]
    )
    def test_update_category(self, is_test, category_id, payload):
        if category_id == "placeholder id":
            category_id = self.get_random_category_id()

        self.update_category(category_id, payload)

        if is_test == "positive":
            assert self.check_response_is(HTTPStatus.OK)
            self.validate_category()
        else:
            assert self.check_response_is(HTTPStatus.UNPROCESSABLE_ENTITY)