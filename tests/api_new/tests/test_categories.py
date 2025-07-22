import pytest

from tests.api_new.services.categories.create_category import CreateCategory
from tests.api_new.services.categories.delete_category import DeleteCategory
from tests.api_new.services.categories.get_all_categories import GetAllCategories
from tests.api_new.services.categories.get_category import GetCategory
from tests.api_new.services.categories.payloads import payloads
from tests.api_new.services.categories.update_category import UpdateCategory


class TestCategories(DeleteCategory, UpdateCategory, GetAllCategories, CreateCategory, GetCategory):

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
        self.create_category(payload)
        if is_test == "positive":
            assert self.check_response_is(200)
            self.validate_category()
        else:
            assert self.check_response_is(422)

    @pytest.mark.parametrize(
        "is_test, category_id",
        [
            ("positive", None),  # None will be replaced by real id after
            ("negative", "wrong id"),
            ("negative", 12345678),
        ]
    )
    def test_get_category_by_id(self, is_test, category_id):
        if category_id is None:
            category_id = self.get_random_category_id()

        self.get_category_by_id(category_id)
        if is_test == "positive":
            assert self.check_response_is(200)
            self.validate_category()
        else:
            assert self.check_response_is(422)

    def test_get_all_categories(self):
        self.get_all_categories()
        assert self.check_response_is(200)
        self.validate_list_of_categories()

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
        if category_id is None:
            category_id = self.get_random_category_id()

        self.update_category(category_id, payload)
        if is_test == "positive":
            assert self.check_response_is(200)
            self.validate_category()
        else:
            assert self.check_response_is(422)

    @pytest.mark.parametrize(
        "is_test, category_id",
        [
            ("positive", None),
            ("negative", "wrong id"),
        ]
    )
    def test_delete_category(self, is_test, category_id):
        if category_id is None:
            category_id = self.get_random_category_id()

        self.delete_category(category_id)

        if is_test == "positive":
            assert self.check_response_is(200)
            assert self.is_category_deleted(category_id)
        else:
            assert self.check_response_is(422)

