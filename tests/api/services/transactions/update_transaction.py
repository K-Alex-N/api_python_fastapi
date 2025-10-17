import allure

from tests.api.services.transactions.base_transaction import TransactionEndpoint
from tests.api.services.transactions.urls import url


class UpdateTransaction(TransactionEndpoint):
    @allure.step("Update transaction by id: {transaction_id} with payload: {payload}")
    def update_transaction(self, transaction_id, payload) -> None:
        self.response = self.client.patch(
            url=url.update_transaction(transaction_id), json=payload
        )
        self.process_response()
