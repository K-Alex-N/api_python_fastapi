import allure

from tests.api.services.transactions.base_transaction import TransactionEndpoint
from tests.api.services.transactions.urls import url


class GetTransaction(TransactionEndpoint):
    @allure.step("Get transaction by id: {transaction_id}")
    async def get_transaction_by_id(self, transaction_id) -> None:
        self.response = await self.client.get(url=url.get_transaction_by_id(transaction_id))
        await self.process_response()
