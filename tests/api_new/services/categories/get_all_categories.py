import random

import requests

from app.api.categories.schemas import CategoryOutList
from tests.api_new.common.base_test import BaseTest
from tests.api_new.common.helper import Helper
from tests.api_new.services.categories.urls import urls


class GetAllCategories(BaseTest, Helper):

    def get_all_categories(self):
        self.response = requests.get(
            url=urls.get_all_categories
        )

        self.response_json = self.response.json()
        self.attach_response(self.response_json)
        return self.response

    def validate_list_of_categories(self):
        CategoryOutList.model_validate(self.response_json)

    def get_random_category_id(self):
        categories = self.get_all_categories().json()
        l = len(categories)
        return categories[random.randrange(0, l)]["id"]