import requests

from app.api.categories.schemas import CategoryOut
from tests.api_new.common.base_test import BaseTest
from tests.api_new.common.helper import Helper
from tests.api_new.services.categories.urls import urls


class GetCategory(BaseTest, Helper):

    def get_category_by_id(self, category_id):
        self.response = requests.get(
            url=urls.get_category_by_id(category_id)
        )
        self.response_json = self.response.json()
        self.attach_response(self.response_json)

    def validate_category(self):
        CategoryOut.model_validate(self.response_json)