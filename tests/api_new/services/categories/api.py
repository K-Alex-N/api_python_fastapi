import requests

from app.api.categories.schemas import CategoryOut
from tests.api_new.common.config import BASE_URL
from tests.api_new.common.helper import Helper
from tests.api_new.services.categories.payloads import Payloads



class CategoriesAPI(Helper):

    def __init__(self):
        super().__init__()
        self.payloads = Payloads()
        self.url = f"{BASE_URL}/categories/"

    def create_category(self):
        response = requests.post(
            url=self.url,
            json=self.payloads.create_category,
        )

        assert response.status_code == 200, response.json()
        return CategoryOut(**response.json())
