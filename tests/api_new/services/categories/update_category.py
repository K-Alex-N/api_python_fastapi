import requests

from app.api.categories.schemas import CategoryOut
from tests.api_new.common.base_test import BaseTest
from tests.api_new.common.helper import Helper
from tests.api_new.services.categories.endpoints import endpoints


class UpdateCategory(BaseTest, Helper):

    def update_category(self, category_id, payload):
        self.response = requests.patch(
            url=endpoints.update_category(category_id),
            json=payload
        )

        self.response_json = self.response.json()
        self.attach_response(self.response_json)


    def validate_category(self):
        CategoryOut.model_validate(self.response_json)