from http import HTTPStatus

import allure
import pytest

from tests.api.services.transactions.delete_transaction import DeleteTransaction
from tests.api.services.transactions.get_all_transactions import GetAllTransactions


@allure.epic("API")
@allure.feature("Transaction")
@allure.story("DeleteTransaction")
class TestDeleteTransaction(DeleteTransaction, GetAllTransactions):

    @pytest.mark.parametrize(
        "is_test, transaction_id",
        [
            ("positive", "placeholder id"),  # will be replaced by real id
            ("-negative", "wrong id"),
        ],
    )
    def test_delete_transaction(self, is_test, transaction_id) -> None:
        if transaction_id == "placeholder id":
            transaction_id = self.get_random_transaction_id()

        self.delete_transaction(transaction_id)

        if is_test == "positive":
            assert self.check_response_is(HTTPStatus.OK)
            assert self.is_transaction_deleted(transaction_id)
        else:
            assert self.check_response_is(HTTPStatus.UNPROCESSABLE_ENTITY)
