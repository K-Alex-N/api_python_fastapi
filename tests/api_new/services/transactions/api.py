import requests

from app.api.transactions.schemas import TransactionOut, TransactionOutList

from tests.api_new.common.helper import Helper
from tests.api_new.services.categories.api import CategoriesAPI
from tests.api_new.services.transactions.endpoints import Endpoints
from tests.api_new.services.transactions.payloads import payload_create_transaction


class TransactionsAPI(Helper):
    endpoints = Endpoints()

    category = CategoriesAPI()

    def create_transaction(self):
        payload = payload_create_transaction()
        category = self.category.create_category()
        print("\n\n\n", payload)
        payload["category_id"] = str(category.id)
        print("\n\n\n", payload)
        response = requests.post(
            url=self.endpoints.create_transaction,
            json=payload,
        )

        assert response.status_code == 200, response.json()
        return TransactionOut.model_validate(response.json())

    def get_all_transactions(self) -> TransactionOutList:
        response = requests.get(url=self.endpoints.get_all_transactions)

        assert response.status_code == 200, response.json()
        return TransactionOutList.model_validate(response.json())

    def get_transaction_by_id(self, transaction_id):
        response = requests.get(
            url=self.endpoints.get_transaction_by_id(transaction_id)
        )

        assert response.status_code == 200, response.json()

    def update_transaction(self, transaction_id):
        response = requests.patch(
            url=self.endpoints.update_transaction(transaction_id),
            json=self.payloads.create_transaction
        )

        assert response.status_code == 200, response.json()

    def delete_transaction(self, transaction_id):
        response = requests.delete(
            url=self.endpoints.delete_transaction(transaction_id)
        )

        assert response.status_code == 200, response.json()
