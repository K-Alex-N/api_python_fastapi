import allure
from app.api.categories.schemas import CategoryOut, CategoryOutList
from tests.api.base_endpoint import BaseEndpoint

class CategoryEndpoint(BaseEndpoint):
    @allure.step("Validate category response")
    async def validate_category(self) -> None:

        data_to_validate = self._extract_category_data(self.response_json)
        original_response_json = self.response_json
        self.response_json = data_to_validate
        await self.validate(CategoryOut)
        self.response_json = original_response_json

    @allure.step("Validate list of categories response")
    async def validate_list_of_categories(self) -> None:
        if self.response.status_code >= 400:
            allure.attach(
                f"Skipping validation due to error status: {self.response.status_code}",
                name="Validation Skipped",
                attachment_type=allure.attachment_type.TEXT,
            )
            return
        
        data_to_validate = self._extract_categories_list(self.response_json)
        original_response_json = self.response_json
        self.response_json = data_to_validate
        await self.validate(CategoryOutList)
        self.response_json = original_response_json
    
    def _extract_category_data(self, response_data):
        if isinstance(response_data, dict):
            if "category" in response_data:
                return response_data["category"]
            elif "data" in response_data:
                return response_data["data"]
            for value in response_data.values():
                if isinstance(value, dict) and "id" in value:
                    return value
        return response_data
    
    def _extract_categories_list(self, response_data):
        if isinstance(response_data, dict):
            if "categories" in response_data:
                return response_data["categories"]
            elif "data" in response_data:
                return response_data["data"]
            for value in response_data.values():
                if isinstance(value, list):
                    return value
        return response_data
