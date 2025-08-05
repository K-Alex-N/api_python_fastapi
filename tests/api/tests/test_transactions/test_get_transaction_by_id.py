from http import HTTPStatus

import allure
import pytest

from tests.api.services.transactions.get_all_transactions import GetAllTransactions
from tests.api.services.transactions.get_transaction import GetTransaction

@allure.epic("API")
@allure.feature("Transaction")
@allure.story("GetTransaction")
class TestGetTransaction(GetTransaction, GetAllTransactions):

    @pytest.mark.parametrize(
        "is_test, transaction_id",
        [
            ("positive", "placeholder id"),
            ("-negative", "wrong id"),
            ("-negative", 12345678),
        ]
    )
    def test_get_transaction_by_id(self, is_test, transaction_id):
        if transaction_id == "placeholder id":
            transaction_id = self.get_random_transaction_id()

        self.get_transaction_by_id(transaction_id)

        if is_test == "positive":
            assert self.check_response_is(HTTPStatus.OK)
            self.validate_transaction()
        else:
            assert self.check_response_is(HTTPStatus.UNPROCESSABLE_ENTITY)
