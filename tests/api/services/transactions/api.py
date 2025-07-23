import requests
from pydantic import UUID4

from app.api.transactions.schemas import TransactionOut, TransactionOutList

from tests.api.services.transactions.payloads import payload_create_transaction


class TransactionsAPI(Helper):
    category = CategoriesAPI()

    def create_transaction(self) -> TransactionOut:
        category = self.category.create_category()
        response = requests.post(
            url=endpoints.create_transaction,
            json=payload_create_transaction(category_id=str(category.id))
        )
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        return TransactionOut.model_validate(response.json())

    def get_all_transactions(self) -> TransactionOutList:
        response = requests.get(url=endpoints.get_all_transactions)
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        return TransactionOutList.model_validate(response.json())

    def get_transaction_by_id(self, transaction_id: UUID4) -> TransactionOut:
        response = requests.get(url=endpoints.get_transaction_by_id(transaction_id))
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        return TransactionOut.model_validate(response.json())

    def update_transaction(self, transaction_id) -> TransactionOut:
        response = requests.patch(
            url=endpoints.update_transaction(transaction_id),
            json=payload_create_transaction()
        )
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        return TransactionOut.model_validate(response.json())

    def delete_transaction(self, transaction_id):
        response = requests.delete(url=endpoints.delete_transaction(transaction_id))
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
