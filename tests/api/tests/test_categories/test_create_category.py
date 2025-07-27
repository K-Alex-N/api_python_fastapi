from http import HTTPStatus

import pytest

from tests.api.services.categories.create_category import CreateCategory
from tests.api.services.categories.payloads import payloads


class TestCreateCategory(CreateCategory):

    @pytest.mark.parametrize(
        "is_test, payload",
        [
            ("positive", payloads.category()),
            ("-negative", payloads.category_without_name()),
            ("-negative", payloads.category_without_type()),
            ("-negative", payloads.category_with_wrong_name()),
            ("-negative", payloads.category_with_wrong_type()),
        ]
    )
    def test_create_category(self, is_test, payload):
        self.create_category(payload)

        if is_test == "positive":
            assert self.check_response_is(HTTPStatus.OK)
            self.validate_category()
        else:
            assert self.check_response_is(HTTPStatus.UNPROCESSABLE_ENTITY)