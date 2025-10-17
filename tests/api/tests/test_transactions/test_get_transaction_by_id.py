from http import HTTPStatus

import allure
import pytest

from tests.api.services.transactions.get_all_transactions import GetAllTransactions
from tests.api.services.transactions.get_transaction import GetTransaction


@allure.epic("API")
@allure.feature("Transaction")
@allure.story("GetTransaction")
class TestGetTransaction(GetTransaction, GetAllTransactions):
    def test_get_transaction_by_id_success(self) -> None:
        transaction_id = self.get_random_transaction_id()
        self.get_transaction_by_id(transaction_id)

        assert self.check_response_is(HTTPStatus.OK)
        self.validate_transaction()

    @pytest.mark.parametrize(
        "transaction_id",
        [
            "wrong id",
            12345678,
        ],
    )
    def test_get_transaction_by_id_fails(self, transaction_id) -> None:
        self.get_transaction_by_id(transaction_id)

        assert self.check_response_is(HTTPStatus.UNPROCESSABLE_ENTITY)
