from http import HTTPStatus

import allure

from tests.api.services.categories.get_all_categories import GetAllCategories


@allure.epic("API")
@allure.feature("Category")
@allure.story("GetAllCategories")
class TestGetAllCategories(GetAllCategories):

    def test_get_all_categories(self) -> None:
        self.get_all_categories()
        assert self.check_response_is(HTTPStatus.OK)
        self.validate_list_of_categories()
