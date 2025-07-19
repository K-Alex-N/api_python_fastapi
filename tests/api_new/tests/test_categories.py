from tests.api_new.common.base_test import BaseTest


class TestCategories(BaseTest):

    def test_create_category(self):
        self.api.create_category()