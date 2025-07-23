import allure

from app.api.categories.schemas import CategoryOut, CategoryOutList
from tests.api_new.common.base_endpoint import BaseEndpoint


class CategoryEndpoint(BaseEndpoint):

    def _validate(self, schema):
        schema.model_validate(self.response_json)

    @allure.step("Validate response against schema CategoryOut")
    def validate_category(self):
        # self._validate(CategoryOut)
        CategoryOut.model_validate(self.response_json)

    @allure.step("Validate response against schema CategoryOutList")
    def validate_list_of_categories(self):
        CategoryOutList.model_validate(self.response_json)