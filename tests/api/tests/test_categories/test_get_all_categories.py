from http import HTTPStatus

from tests.api.services.categories.get_all_categories import GetAllCategories


class TestCategories(GetAllCategories):

    def test_get_all_categories(self):
        self.get_all_categories()
        assert self.check_response_is(HTTPStatus.OK)
        self.validate_list_of_categories()
