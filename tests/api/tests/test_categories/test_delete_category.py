from http import HTTPStatus

import allure
import pytest

from tests.api.services.categories.delete_category import DeleteCategory
from tests.api.services.categories.get_all_categories import GetAllCategories


class TestDeleteCategory(DeleteCategory, GetAllCategories):

    @allure.epic()
    @pytest.mark.parametrize(
        "is_test, category_id",
        [
            ("positive", "placeholder id"), # will be replaced by real id after
            ("negative", "wrong id"),
        ]
    )
    def test_delete_category(self, is_test, category_id):
        if category_id == "placeholder id":
            category_id = self.get_random_category_id()

        self.delete_category(category_id)

        if is_test == "positive":
            assert self.check_response_is(HTTPStatus.OK)
            assert self.is_category_deleted(category_id)
        else:
            assert self.check_response_is(HTTPStatus.UNPROCESSABLE_ENTITY)
