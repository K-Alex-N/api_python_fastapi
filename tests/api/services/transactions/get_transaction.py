import allure
import requests

from tests.api.services.transactions.base_transaction import TransactionEndpoint
from tests.api.services.transactions.urls import url


class GetTransaction(TransactionEndpoint):

    @allure.step("Get transaction by id: {transaction_id}")
    def get_transaction_by_id(self, transaction_id):
        self.response = requests.get(
            url=url.get_transaction_by_id(transaction_id)
        )
        self._process_response()
