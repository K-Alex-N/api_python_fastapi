import allure

from tests.api.services.transactions.base_transaction import TransactionEndpoint
from tests.api.services.transactions.urls import url


class CreateTransaction(TransactionEndpoint):
    @allure.step("Create transaction with payload: {payload}")
    async def create_transaction(self, payload) -> None:
        self.response = await self.client.post(url=url.create_transaction, json=payload)
        await self.process_response()
