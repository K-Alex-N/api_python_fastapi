import allure

from tests.api.services.transactions.base_transaction import TransactionEndpoint
from tests.api.services.transactions.urls import url


class UpdateTransaction(TransactionEndpoint):
    @allure.step("Update transaction with id: {transaction_id}")
    async def update_transaction(self, transaction_id, payload) -> None:
        self.response = await self.client.patch(
            url=url.update_transaction(transaction_id), json=payload
        )
        await self.process_response()
