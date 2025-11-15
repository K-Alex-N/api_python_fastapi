import random
import uuid

import allure

from tests.api.services.transactions.base_transaction import TransactionEndpoint
from tests.api.services.transactions.urls import url


class GetAllTransactions(TransactionEndpoint):
    @allure.step("Get all transactions")
    async def get_all_transactions(self, limit: int = 5):
        params = {"limit": limit}
        self.response = await self.client.get(url=url.get_all_transactions, params=params)
        await self.process_response()
        return self.response

    @allure.step("Get random transaction id")
    async def get_random_transaction_id(self) -> uuid.UUID:
        await self.get_all_transactions()
        response_data = self.response_json

        if isinstance(response_data, dict):
            if "transactions" in response_data:
                transactions = response_data["transactions"]
            elif "data" in response_data:
                transactions = response_data["data"]
            else:
                transactions = None
                for value in response_data.values():
                    if isinstance(value, list) and len(value) > 0:
                        transactions = value
                        break
                if transactions is None:
                    raise ValueError(f"No transactions found in response: {response_data}")
        elif isinstance(response_data, list):
            transactions = response_data
        else:
            raise ValueError(f"Unexpected response format: {response_data}")

        if not transactions or len(transactions) == 0:
            raise ValueError("No transactions found")
        
        random_transaction_number = random.randint(0, len(transactions) - 1)
        transaction_item = transactions[random_transaction_number]
        return transaction_item["id"]
