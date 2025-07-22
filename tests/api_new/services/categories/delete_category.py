import requests

from tests.api_new.common.base_test import BaseTest
from tests.api_new.common.helper import Helper
from tests.api_new.services.categories.urls import urls
from tests.api_new.services.categories.get_category import GetCategory


class DeleteCategory(BaseTest, Helper):
    def delete_category(self, category_id):
        self.response = requests.delete(
            url=urls.delete_category(category_id)
        )

        self.response_json = self.response.json()
        self.attach_response(self.response_json)

    @staticmethod
    def is_category_deleted(category_id):
        get_endpoint = GetCategory()
        category = get_endpoint.get_category_by_id(category_id)
        return True if not category else False
