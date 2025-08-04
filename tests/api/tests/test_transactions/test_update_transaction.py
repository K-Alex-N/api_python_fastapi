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
        "is_test, transaction_id, payload",
        [
            ("positive", "placeholder id", payloads.create_transaction),
            ("positive", "placeholder id", payloads.create_transaction_without_amount),
            ("positive", "placeholder id", payloads.create_transaction_without_date),
            ("positive", "placeholder id", payloads.create_transaction_without_description),
            ("positive", "placeholder id", payloads.create_transaction_without_category_id),
            ("-negative", "placeholder id", payloads.create_transaction_with_wrong_amount),
            ("-negative", "placeholder id", payloads.create_transaction_with_wrong_date),
            ("-negative", "placeholder id", payloads.create_transaction_with_wrong_description),
            ("-negative", "placeholder id", payloads.create_transaction_with_wrong_category_id),
            ("-negative", "wrong id", payloads.create_transaction),
            ("-negative", 12345678, payloads.create_transaction),
        ]
    )
    def test_update_transaction(self, is_test, transaction_id, payload):
        if transaction_id == "placeholder id":
            transaction_id = self.get_random_transaction_id()

        self.update_transaction(transaction_id, payload())

        if is_test == "positive":
            assert self.check_response_is(HTTPStatus.OK)
            self.validate_transaction()
        else:
            assert self.check_response_is(HTTPStatus.UNPROCESSABLE_ENTITY)
