import uuid

import allure
import requests

from tests.api.services.transactions.base_transaction import TransactionEndpoint
from tests.api.services.transactions.urls import url


class GetAllTransactions(TransactionEndpoint):

    @allure.step("Get all transactions")
    def get_all_transactions(self, limit: int = 5):
        params = {"limit": limit}
        self.response = requests.get(url=url.get_all_transactions, params=params)
        self.process_response()
        return self.response

    @allure.step("Get random transaction id")
    def get_random_transaction_id(self) -> uuid.UUID:
        transactions = self.get_all_transactions(limit=1).json()
        return transactions[0]["id"]
