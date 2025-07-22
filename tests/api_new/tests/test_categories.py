import pytest

from tests.api_new.services.categories.api import CategoriesAPI
from tests.api_new.services.categories.create_category import CreateCategory
from tests.api_new.services.categories.payloads import payloads


class TestCategories(CategoriesAPI, CreateCategory):

    @pytest.mark.skip
    @pytest.mark.parametrize(
        "is_test, payload",
        [
            ("positive", payloads.category()),
            ("negative", payloads.category_without_name()),
            ("negative", payloads.category_without_type()),
            ("negative", payloads.category_with_wrong_name()),
            ("negative", payloads.category_with_wrong_type()),
        ]
    )
    def test_create_category(self, is_test, payload):

        # self.create_category(is_test, payload)
        create_category_endpoint = CreateCategory()
        create_category_endpoint.create_category(payload)
        # self.create_category(payload) - попробовать все через self прописать
        if is_test == "positive":
            assert create_category_endpoint.check_response_is(200)
            create_category_endpoint.validate()
        else:
            assert create_category_endpoint.check_response_is(422)

    @pytest.mark.skip
    @pytest.mark.parametrize(
        "is_test, category_id",
        [
            ("positive", None),  # None will be replaced by real id after
            ("negative", "wrong id"),
            ("negative", 12345678),
        ]
    )
    def test_get_category_by_id(self, is_test, category_id):
        self.get_category_by_id(is_test, category_id)

    @pytest.mark.skip
    def test_get_all_categories(self):
        self.get_all_categories()

    #     @pytest.mark.skip

    @pytest.mark.parametrize(
        "is_test, category_id, payload",
        [
            ("positive", None, payloads.category()),
            ("positive", None, payloads.category_without_name()),
            ("positive", None, payloads.category_without_type()),
            ("positive", None, payloads.category_without_name_and_type()),
            ("negative", None, payloads.category_with_wrong_name()),
            ("negative", None, payloads.category_with_wrong_type()),
            ("negative", "wrong is", payloads.category()),
            ("negative", 12345678, payloads.category_without_name()),
        ]
    )
    def test_update_category(self, is_test, category_id, payload):
        self.update_category(is_test, category_id, payload)

    @pytest.mark.skip
    def test_delete_category(self):
        category_id = self.get_one_category_id()
        # get_category_id_if_category_id_is_None()
        self.delete_category(category_id)
