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
        # First try to get existing transactions
        try:
            await self.get_all_transactions()
            response_data = self.response_json

            # Check if response is an error message
            if isinstance(response_data, dict) and "message" in response_data:
                raise ValueError(f"API returned error: {response_data.get('message', 'Unknown error')}")
        except ValueError as e:
            if "API returned error" in str(e):
                # If there's an error getting transactions, create one first
                from tests.api.services.transactions.create_transaction import CreateTransaction
                from tests.api.services.transactions.payloads import Payloads

                create_trx = CreateTransaction(self.client)
                payloads = Payloads(self.client)
                await create_trx.create_transaction(await payloads.create_transaction())

                # Return the ID of the newly created transaction
                if isinstance(create_trx.response_json, dict) and "id" in create_trx.response_json:
                    return uuid.UUID(str(create_trx.response_json["id"]))
                else:
                    raise ValueError("Failed to get ID from created transaction")
            else:
                raise

        # Handle different response structures
        if isinstance(response_data, dict):
            # If response is {"transactions": [...]} or similar structure
            if "transactions" in response_data:
                transactions = response_data["transactions"]
            elif "data" in response_data:
                transactions = response_data["data"]
            else:
                # Try to find the first list value in the dict
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
        if isinstance(transaction_item, dict) and "id" in transaction_item:
            return transaction_item["id"]
        else:
            raise ValueError(f"Transaction item is not in expected format: {transaction_item}")
