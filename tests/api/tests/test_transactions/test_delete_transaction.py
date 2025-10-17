from http import HTTPStatus

import allure
import pytest

from tests.api.services.transactions.delete_transaction import DeleteTransaction
from tests.api.services.transactions.get_all_transactions import GetAllTransactions


@allure.epic("API")
@allure.feature("Transaction")
@allure.story("DeleteTransaction")
class TestDeleteTransaction(DeleteTransaction, GetAllTransactions):
    def test_delete_transaction_success(self) -> None:
        transaction_id = self.get_random_transaction_id()
        self.delete_transaction(transaction_id)

        assert self.check_response_is(HTTPStatus.OK)
        assert self.is_transaction_deleted(transaction_id)

    @pytest.mark.parametrize(
        "transaction_id",
        [
            "wrong id",
        ],
    )
    def test_delete_transaction_fails(self, transaction_id) -> None:
        self.delete_transaction(transaction_id)

        assert self.check_response_is(HTTPStatus.UNPROCESSABLE_ENTITY)
