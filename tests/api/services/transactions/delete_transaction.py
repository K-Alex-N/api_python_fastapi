import allure
import requests

from tests.api.services.transactions.base_transaction import TransactionEndpoint
from tests.api.services.transactions.get_transaction import GetTransaction
from tests.api.services.transactions.urls import url


class DeleteTransaction(TransactionEndpoint):

    @allure.step("Delete transaction by id: {transaction_id}")
    def delete_transaction(self, transaction_id):
        self.response = requests.delete(
            url=url.delete_transaction(transaction_id)
        )
        self.process_response()

    @staticmethod
    @allure.step("Check if transaction with id {transaction_id} deleted")
    def is_transaction_deleted(transaction_id):
        response = GetTransaction().get_transaction_by_id(transaction_id)
        return True if not response else False
