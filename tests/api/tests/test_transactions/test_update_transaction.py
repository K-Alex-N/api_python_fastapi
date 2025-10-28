from collections.abc import Callable
from http import HTTPStatus

import allure
import pytest

from tests.api.services.transactions.get_all_transactions import GetAllTransactions
from tests.api.services.transactions.payloads import payloads
from tests.api.services.transactions.update_transaction import UpdateTransaction


@allure.epic("API")
@allure.feature("Transaction")
@allure.story("UpdateTransaction")
class TestUpdateTransaction(UpdateTransaction, GetAllTransactions):
    @pytest.mark.parametrize(
        "payload",
        [
            payloads.create_transaction,
            payloads.create_transaction_without_amount,
            payloads.create_transaction_without_date,
            payloads.create_transaction_without_description,
            payloads.create_transaction_without_category_id,
        ],
    )
    def test_update_transaction_success(self, payload) -> None:
        transaction_id = self.get_random_transaction_id()
        self.update_transaction(transaction_id, payload())

        assert self.check_response_is(HTTPStatus.OK)
        self.validate_transaction()

    @pytest.mark.parametrize(
        "transaction_id, payload",
        [
            ("placeholder id", payloads.create_transaction_with_wrong_amount),
            ("placeholder id", payloads.create_transaction_with_wrong_date),
            ("placeholder id", payloads.create_transaction_with_wrong_description),
            ("placeholder id", payloads.create_transaction_with_wrong_category_id),
            ("wrong id", payloads.create_transaction),
            (12345678, payloads.create_transaction),
        ],
    )
    def test_update_transaction_fails(self, transaction_id, payload: Callable) -> None:
        if transaction_id == "placeholder id":
            transaction_id = self.get_random_transaction_id()

        self.update_transaction(transaction_id, payload())

        assert self.check_response_is(HTTPStatus.UNPROCESSABLE_ENTITY)
