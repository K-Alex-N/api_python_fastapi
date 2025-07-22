import requests
from pydantic import UUID4

from app.api.categories.schemas import CategoryOut, CategoryOutList
from tests.api_new.common.base_test import BaseTest
from tests.api_new.common.helper import Helper
from tests.api_new.services.categories.endpoints import endpoints
from tests.api_new.services.categories.payloads import payloads


class CategoriesAPI(BaseTest, Helper):

    # def create_category(self, is_test, payload) -> CategoryOut | None:
    #     self.response = requests.post(
    #         # response = requests.post(
    #         url=endpoints.create_category,
    #         json=payload
    #     )
    #     self.attach_response(self.response.json())
    #     if is_test == "positive":
    #         # assert response.status_code == 200
    #         assert self.check_response_is(200)
    #         return CategoryOut.model_validate(self.response.json())
    #         # мб от return избавиться. я ведь наверное нигде и не использую возвращенные значения.
    #         # так код чище будет и аннотацию типов на выхоже ка None можно поставить
    #         # тогда и вот этот код в Фикстуру спрятать можно будет - self.attach_response(self.response.json())
    #     else:
    #         # assert response.status_code == 422, response.json()
    #         assert self.check_response_is(422)
    #         return None

    # def get_all_categories(self) -> CategoryOutList:
    #     self.
    #     assert response.status_code == 200, response.json()
    #     return CategoryOutList.model_validate(response.json())

    # def get_one_category_id(self):
    #     categories = self.get_all_categories()
    #     return categories.model_dump()[0]["id"]

    # def get_category_by_id(self, is_test="positive", category_id: UUID4 = None) -> CategoryOut | None:
        # if category_id is None:
        #     category_id = self.get_one_category_id()


        # if is_test == "positive":
        #     assert response.status_code == 200, response.json()
        #     return CategoryOut.model_validate(response.json())
        # else:
        #     assert response.status_code == 422, response.json()
        #     return None

    def update_category(self, is_test, category_id, payload) -> CategoryOut | None:
        if not category_id: # а если подать пустую строку то тоже пройдет условие?
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
        # check that there is no anymore this id in DB
        # for this

