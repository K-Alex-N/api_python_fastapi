import allure
import requests

from tests.api.services.transactions.base_transaction import TransactionEndpoint
from tests.api.services.transactions.urls import url


class UpdateTransaction(TransactionEndpoint):

    @allure.step("Update transaction by id: {transaction_id} with payload: {payload}")
    def update_transaction(self, transaction_id, payload):
        self.response = requests.patch(
            url=url.update_transaction(transaction_id),
            json=payload
        )

        self.response_json = self.response.json()
        self.allure_attach_response(self.response_json)
