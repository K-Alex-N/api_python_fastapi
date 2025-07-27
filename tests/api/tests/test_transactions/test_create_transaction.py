from http import HTTPStatus

import pytest

from tests.api.services.transactions.create_transaction import CreateTransaction
from tests.api.services.transactions.payloads import payloads


class TestCreateTransaction(CreateTransaction):

    @pytest.mark.parametrize(
        "is_test, payload",
        [
            ("positive", payloads.create_transaction),
            ("-negative", payloads.create_transaction_without_amount),
            ("-negative", payloads.create_transaction_without_date),
            ("-negative", payloads.create_transaction_without_description),
            ("-negative", payloads.create_transaction_without_category_id),
            ("-negative", payloads.create_transaction_with_wrong_amount),
            ("-negative", payloads.create_transaction_with_wrong_date),
            ("-negative", payloads.create_transaction_with_wrong_description),
            ("-negative", payloads.create_transaction_with_wrong_category_id),
        ]
    )
    def test_create_transaction(self, is_test, payload):
        self.create_transaction(payload())

        if is_test == "positive":
            assert self.check_response_is(HTTPStatus.OK)
            self.validate_transaction()
        else:
            assert self.check_response_is(HTTPStatus.UNPROCESSABLE_ENTITY)
