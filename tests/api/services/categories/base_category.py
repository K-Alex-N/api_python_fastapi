from app.api.categories.schemas import CategoryOut, CategoryOutList
from tests.api.base_endpoint import BaseEndpoint


class CategoryEndpoint(BaseEndpoint):

    def validate_category(self):
        self.validate(CategoryOut)

    def validate_list_of_categories(self):
        self.validate(CategoryOutList)
