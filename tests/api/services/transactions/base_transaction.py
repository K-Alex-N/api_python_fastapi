import allure

from app.api.transactions.schemas import TransactionOut, TransactionOutList
from tests.api.base_endpoint import BaseEndpoint


class TransactionEndpoint(BaseEndpoint):
    @allure.step("Validate transaction response")
    async def validate_transaction(self) -> None:
        data_to_validate = self._extract_transaction_data(self.response_json)
        original_response_json = self.response_json
        self.response_json = data_to_validate
        await self.validate(TransactionOut)
        self.response_json = original_response_json

    @allure.step("Validate list of transactions response")
    async def validate_list_of_transactions(self) -> None:
        data_to_validate = self._extract_transactions_list(self.response_json)
        original_response_json = self.response_json
        self.response_json = data_to_validate
        await self.validate(TransactionOutList)
        self.response_json = original_response_json

    @staticmethod
    def _extract_transaction_data(response_data):
        if isinstance(response_data, dict):
            if "transaction" in response_data:
                return response_data["transaction"]
            elif "data" in response_data:
                return response_data["data"]
            if "amount" in response_data and "date" in response_data:
                return response_data
        return response_data

    @staticmethod
    def _extract_transactions_list(response_data):
        if isinstance(response_data, dict):
            if "transactions" in response_data:
                return response_data["transactions"]
            elif "data" in response_data:
                return response_data["data"]
            for value in response_data.values():
                if isinstance(value, list):
                    return value
        return response_data
