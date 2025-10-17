from http import HTTPStatus

import allure
import pytest

from tests.api.services.transactions.create_transaction import CreateTransaction
from tests.api.services.transactions.payloads import payloads


@allure.epic("API")
@allure.feature("Transaction")
@allure.story("CreateTransaction")
class TestCreateTransaction(CreateTransaction):
    def test_create_transaction_success(self) -> None:
        self.create_transaction(payloads.create_transaction())

        assert self.check_response_is(HTTPStatus.OK)
        self.validate_transaction()

    @pytest.mark.parametrize(
        "payload",
        [
            payloads.create_transaction_without_amount,
            payloads.create_transaction_without_date,
            payloads.create_transaction_without_description,
            payloads.create_transaction_without_category_id,
            payloads.create_transaction_with_wrong_amount,
            payloads.create_transaction_with_wrong_date,
            payloads.create_transaction_with_wrong_description,
            payloads.create_transaction_with_wrong_category_id,
        ],
    )
    def test_create_transaction_fails(self, payload) -> None:
        self.create_transaction(payload())

        assert self.check_response_is(HTTPStatus.UNPROCESSABLE_ENTITY)