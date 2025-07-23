import allure
import requests

from tests.api.services.transactions.base_transaction import TransactionEndpoint
from tests.api.services.transactions.urls import url


class CreateTransaction(TransactionEndpoint):

    @allure.step("Create transaction with payload: {payload}")
    def create_transaction(self, payload):
        self.response = requests.post(
            url=url.create_transaction,
            json=payload
        )
        self.response_json = self.response.json()
        self.allure_attach_response(self.response_json)