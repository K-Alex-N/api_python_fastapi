import requests
from pydantic import UUID4

from app.api.categories.schemas import CategoryOut, CategoryOutList
from tests.api_new.common.helper import Helper
from tests.api_new.services.categories.endpoints import endpoints
from tests.api_new.services.categories.payloads import payloads


class CategoriesAPI(Helper):

    # def create_category(self, payload, expected_status=200, is_validate=True):
    #     response = requests.post(
    #         url=endpoints.create_category,
    #         json=payload
    #     )
    #     assert response.status_code == expected_status, response.json()
    #     self.attach_response(response.json())
    #     return CategoryOut.model_validate(response.json()) if is_validate else None

    def create_category(self, is_test, payload) -> CategoryOut | None:
        response = requests.post(
            url=endpoints.create_category,
            json=payload
        )
        self.attach_response(response.json())
        if is_test == "positive":
            assert response.status_code == 200, response.json()
            return CategoryOut.model_validate(response.json())
        else:
            assert response.status_code == 422, response.json()
            return None

    def get_all_categories(self) -> CategoryOutList:
        response = requests.get(url=endpoints.get_all_categories)
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        return CategoryOutList.model_validate(response.json())

    def get_one_category_id(self):
        categories = self.get_all_categories()
        return categories.model_dump()[0]["id"]

    def get_category_by_id(self, is_test="positive", category_id: UUID4 = None) -> CategoryOut | None:
        if not category_id:
            category_id = self.get_one_category_id()
        response = requests.get(url=endpoints.get_category_by_id(category_id))
        self.attach_response(response.json())

        if is_test == "positive":
            assert response.status_code == 200, response.json()
            return CategoryOut.model_validate(response.json())
        else:
            assert response.status_code == 422, response.json()
            return None

    def update_category(self, is_test, category_id, payload) -> CategoryOut | None:
        if not category_id:
            category_id = self.get_one_category_id()

        response = requests.patch(
            url=endpoints.update_category(category_id),
            json=payload
        )
        self.attach_response(response.json())

        if is_test == "positive":
            assert response.status_code == 200, response.json()
            return CategoryOut.model_validate(response.json())
        else:
            assert response.status_code == 422, response.json()
            return None

    def delete_category(self, category_id: UUID4) -> None:
        response = requests.delete(url=endpoints.delete_category(category_id))
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
