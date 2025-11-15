import allure

from tests.api.services.transactions.base_transaction import TransactionEndpoint
from tests.api.services.transactions.get_transaction import GetTransaction
from tests.api.services.transactions.urls import url


class DeleteTransaction(TransactionEndpoint):
    @allure.step("Delete transaction with id: {transaction_id}")
    async def delete_transaction(self, transaction_id) -> None:
        self.response = await self.client.delete(
            url=url.delete_transaction(transaction_id)
        )
        await self.process_response()

    @allure.step("Check if transaction with id {transaction_id} deleted")
    async def is_transaction_deleted(self, transaction_id) -> bool:
        get_transaction = GetTransaction(self.client)
        await get_transaction.get_transaction_by_id(transaction_id)
        return get_transaction.response.status_code == 404
