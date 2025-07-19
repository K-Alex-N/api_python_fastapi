import requests
from pydantic import UUID4

from app.api.categories.schemas import CategoryOut, CategoryOutList
from tests.api_new.common.helper import Helper
from tests.api_new.services.categories.endpoints import Endpoints
from tests.api_new.services.categories.payloads import category_payload


class CategoriesAPI(Helper):
    endpoints = Endpoints()

    def create_category(self) -> CategoryOut:
        response = requests.post(
            url=self.endpoints.create_category,
            json=category_payload()
        )
        assert response.status_code == 200, response.json()
        return CategoryOut.model_validate(response.json())

    def get_all_categories(self) -> CategoryOutList:
        response = requests.get(
            url=self.endpoints.get_all_categories
        )
        assert response.status_code == 200, response.json()
        return CategoryOutList.model_validate(response.json())

    def get_category_by_id(self, category_id: UUID4) -> CategoryOut:
        response = requests.get(
            url=self.endpoints.get_category_by_id(category_id)
        )
        assert response.status_code == 200, response.json()
        return CategoryOut.model_validate(response.json())

    def update_category(self, category_id: UUID4) -> CategoryOut:
        response = requests.patch(
            url=self.endpoints.update_category(category_id),
            json=category_payload()
        )
        assert response.status_code == 200, response.json()
        return CategoryOut.model_validate(response.json())

    def delete_category(self, category_id: UUID4) -> None:
        response = requests.delete(
            url=self.endpoints.delete_category(category_id)
        )
        assert response.status_code == 200, response.json()
