from http import HTTPStatus

import allure

from tests.api.services.categories.get_all_categories import GetAllCategories


class TestGetAllCategories(GetAllCategories):

    @allure.feature("Get all categories")
    def test_get_all_categories(self):
        self.get_all_categories()
        assert self.check_response_is(HTTPStatus.OK)
        self.validate_list_of_categories()
