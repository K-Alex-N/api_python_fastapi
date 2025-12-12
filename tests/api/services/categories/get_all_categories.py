import random

import allure

from tests.api.services.categories.base_category import CategoryEndpoint
from tests.api.services.categories.urls import url


class GetAllCategories(CategoryEndpoint):
    @allure.step("Get all categories")
    async def get_all_categories(self):
        self.response = await self.client.get(url=url.get_all_categories)
        await self.process_response()
        return self.response

    @allure.step("Get random category id")
    async def get_random_category_id(self):
        await self.get_all_categories()
        response_data = self.response_json

        if isinstance(response_data, dict):
            if "categories" in response_data:
                categories = response_data["categories"]
            elif "data" in response_data:
                categories = response_data["data"]
            else:
                categories = None
                for value in response_data.values():
                    if isinstance(value, list) and len(value) > 0:
                        categories = value
                        break
                if categories is None:
                    raise ValueError(f"No categories found in response: {response_data}")
        elif isinstance(response_data, list):
            categories = response_data
        else:
            raise ValueError(f"Unexpected response format: {response_data}")

        random_category_number = random.randint(0, len(categories) - 1)
        category_item = categories[random_category_number]
        return category_item["id"]
