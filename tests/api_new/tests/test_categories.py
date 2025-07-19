import pytest

from tests.api_new.common.base_test import BaseTest


class TestCategories(BaseTest):

    @pytest.mark.skip
    def test_create_category(self):
        self.api.create_category()

    @pytest.mark.skip
    def test_create_category_with_wrong_type(self):
        pass

    @pytest.mark.skip
    def test_get_category_by_id(self):
        category = self.api.create_category()
        self.api.get_category_by_id(category.id)

    @pytest.mark.skip
    def test_get_category_by_wrong_id(self):
        pass

    @pytest.mark.skip
    def test_get_all_categories(self):
        self.api.create_category()
        self.api.get_all_categories()

    @pytest.mark.skip
    def test_update_category(self):
        category = self.api.create_category()
        self.api.update_category(category.id)

    def test_delete_category(self):
        category = self.api.create_category()
        self.api.delete_category(category.id)
