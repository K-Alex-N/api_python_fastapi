import requests

from app.api.categories.schemas import CategoryOut
from tests.api_new.common.base_test import BaseTest
from tests.api_new.common.helper import Helper
from tests.api_new.services.categories.endpoints import endpoints


class CreateCategory(BaseTest, Helper):
    response = None
    response_json = None

    def create_category(self, payload):
        self.response = requests.post(
            url=endpoints.create_category,
            json=payload
        )
        self.attach_response(self.response_json)

    def validate(self):
        CategoryOut.model_validate(self.response_json)