import pytest

from tests.api_new.services.categories.api import CategoriesAPI
from tests.api_new.services.categories.payloads import payloads


class TestCategories(CategoriesAPI):


    def test_create_category_positive(self):
        self.create_category(payloads.category())

    @pytest.mark.parametrize(
        "payload",
        [
            payloads.category_without_name(),
            payloads.category_without_type(),
            payloads.category_with_wrong_name(),
            payloads.category_with_wrong_type(),
        ]
    )
    def test_create_category_negative(self, payload):
        self.create_category(payload, expected_status=422, is_validate=False)



    @pytest.mark.skip
    def test_create_category_with_wrong_type(self):
        pass

    @pytest.mark.skip
    def test_get_category_by_id(self):
        category = self.create_category()
        self.get_category_by_id(category.id)

    @pytest.mark.skip
    def test_get_category_by_wrong_id(self):
        pass

    @pytest.mark.skip
    def test_get_all_categories(self):
        self.create_category()
        self.get_all_categories()

    @pytest.mark.skip
    def test_update_category(self):
        category = self.create_category()
        self.update_category(category.id)

    @pytest.mark.skip
    def test_delete_category(self):
        category = self.create_category()
        self.delete_category(category.id)
