import random

import allure
import requests

from tests.api.services.transactions.base_transaction import TransactionEndpoint
from tests.api.services.transactions.urls import url


class GetAllTransactions(TransactionEndpoint):

    @allure.step("Get all transactions")
    def get_all_transactions(self):
        self.response = requests.get(
            url=url.get_all_transactions
        )

        self._process_response()
        return self.response

    @allure.step("Get random transaction id")
    def get_random_transaction_id(self):
        transactions = self.get_all_transactions().json()
        l = len(transactions)
        return transactions[random.randrange(0, l)]["id"]
