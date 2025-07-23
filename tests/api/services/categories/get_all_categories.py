import random

import allure
import requests

from tests.api.services.categories.base_category import CategoryEndpoint
from tests.api.services.categories.urls import url


class GetAllCategories(CategoryEndpoint):

    @allure.step("Get all categories")
    def get_all_categories(self):
        self.response = requests.get(
            url=url.get_all_categories
        )
        self._process_response()
        return self.response

    @allure.step("Get random category id")
    def get_random_category_id(self):
        categories = self.get_all_categories().json()
        l = len(categories)
        return categories[random.randrange(0, l)]["id"]
