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
        self.process_response()
        return self.response

    @allure.step("Get random transaction id")
    def get_random_transaction_id(self):
        transactions = self.get_all_transactions().json()
        random_transaction_number = random.randint(0, len(transactions) - 1)
        return transactions[random_transaction_number]["id"]
