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
        # First try to get existing categories
        try:
            await self.get_all_categories()
            response_data = self.response_json
            
            # Check if response is an error message
            if isinstance(response_data, dict) and "message" in response_data:
                raise ValueError(f"API returned error: {response_data.get('message', 'Unknown error')}")
        except ValueError as e:
            if "API returned error" in str(e):
                # If there's an error getting categories, create one first
                from tests.api.services.categories.create_category import CreateCategory
                from tests.api.services.categories.payloads import Payloads
                
                create_cat = CreateCategory(self.client)
                payloads = Payloads()
                await create_cat.create_category(payloads.category())
                
                # Return the ID of the newly created category
                if isinstance(create_cat.response_json, dict) and "id" in create_cat.response_json:
                    return create_cat.response_json["id"]
                else:
                    raise ValueError("Failed to get ID from created category")
            else:
                raise
        
        # Handle different response structures
        if isinstance(response_data, dict):
            # If response is {"categories": [...]} or similar structure
            if "categories" in response_data:
                categories = response_data["categories"]
            elif "data" in response_data:
                categories = response_data["data"]
            else:
                # Try to find the first list value in the dict
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
        
        if not categories or len(categories) == 0:
            raise ValueError("No categories found")
        
        random_category_number = random.randint(0, len(categories) - 1)
        category_item = categories[random_category_number]
        if isinstance(category_item, dict) and "id" in category_item:
            return category_item["id"]
        else:
            raise ValueError(f"Category item is not in expected format: {category_item}")
