import allure
import requests

from tests.api_new.services.transactions.base_transaction import TransactionEndpoint


class DeleteTransaction(TransactionEndpoint):

    @allure.step("Delete transaction by id: {transaction_id}")
    def delete_transaction(self, transaction_id):
        self.response = requests.delete(
            url=url.delete_transaction(transaction_id)
        )
        self.response_json = self.response.json()
        self.attach_response(self.response_json)

    @staticmethod
    @allure.step("Check if transaction with id {transaction_id} deleted")
    def is_transaction_deleted(transaction_id):
        get_endpoint = GetTransaction()
        response = get_endpoint.get_transaction_by_id(transaction_id)
        return True if not response else False
