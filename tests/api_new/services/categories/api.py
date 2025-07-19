import requests

from app.api.categories.schemas import CategoryOut, CategoryOutList

from tests.api_new.common.helper import Helper
from tests.api_new.services.categories.endpoints import Endpoints
from tests.api_new.services.categories.payloads import Payloads


class CategoriesAPI(Helper):

    def __init__(self):
        super().__init__()
        self.payloads = Payloads()
        self.endpoints = Endpoints()

    def create_category(self) -> CategoryOut:
        response = requests.post(
            url=self.endpoints.create_category,
            json=self.payloads.create_category,
        )

        assert response.status_code == 200, response.json()
        return CategoryOut.model_validate(response.json())

    def get_all_categories(self) -> CategoryOutList:
        response = requests.get(url=self.endpoints.get_all_categories)

        assert response.status_code == 200, response.json()
        return CategoryOutList.model_validate(response.json())

    def get_category_by_id(self, category_id):
        response = requests.get(
            url=self.endpoints.get_category_by_id(category_id)
        )

        assert response.status_code == 200, response.json()

    def update_category(self, category_id):
        response = requests.patch(
            url=self.endpoints.update_category(category_id),
            json=self.payloads.create_category
        )

        assert response.status_code == 200, response.json()

    def delete_category(self, category_id):
        response = requests.delete(
            url=self.endpoints.delete_category(category_id)
        )

        assert response.status_code == 200, response.json()
