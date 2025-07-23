import allure

from app.api.transactions.schemas import TransactionOut, TransactionOutList
from tests.api.base_endpoint import BaseEndpoint


class TransactionEndpoint(BaseEndpoint):
    pass

    @allure.step("Validate response against schema TransactionOut")
    def validate_transaction(self):
        TransactionOut.model_validate(self.response_json)

    @allure.step("Validate response against schema TransactionOutList")
    def validate_list_of_transactions(self):
        TransactionOutList.model_validate(self.response_json)