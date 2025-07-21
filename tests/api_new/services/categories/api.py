import requests
from pydantic import UUID4

from app.api.categories.schemas import CategoryOut, CategoryOutList
from tests.api_new.common.helper import Helper
from tests.api_new.services.categories.endpoints import endpoints
from tests.api_new.services.categories.payloads import payloads


class CategoriesAPI(Helper):

    def create_category(self, payload, expected_status=200, is_validate=True):
        response = requests.post(
            url=endpoints.create_category,
            json=payload
        )
        assert response.status_code == expected_status, response.json()
        self.attach_response(response.json())
        if is_validate:
            return CategoryOut.model_validate(response.json())
        return None

    def get_all_categories(self) -> CategoryOutList:
        response = requests.get(url=endpoints.get_all_categories)
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        return CategoryOutList.model_validate(response.json())

    def get_category_by_id(self, category_id: UUID4) -> CategoryOut:
        response = requests.get(url=endpoints.get_category_by_id(category_id))
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        return CategoryOut.model_validate(response.json())

    def update_category(self, category_id: UUID4) -> CategoryOut:
        response = requests.patch(
            url=endpoints.update_category(category_id),
            json=payloads.category()
        )
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        return CategoryOut.model_validate(response.json())

    def delete_category(self, category_id: UUID4) -> None:
        response = requests.delete(url=endpoints.delete_category(category_id))
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
