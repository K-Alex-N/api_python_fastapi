from http import HTTPStatus

import pytest
import requests

from tests.api.services.transactions.create_transaction import CreateTransaction
from tests.api.services.transactions.payloads import payloads
from tests.api.services.transactions.urls import url

class TestCreateTransaction(CreateTransaction):

    @pytest.mark.parametrize(
        "is_test, payload",
        [
            ("positive", payloads.create_transaction()),
            # ("negative", payloads.category_without_name()),
            # ("negative", payloads.category_without_type()),
            # ("negative", payloads.category_with_wrong_name()),
            # ("negative", payloads.category_with_wrong_type()),
        ]
    )
    def test_create_transaction(self, is_test, payload):
        self.response = requests.post(
            url=url.create_transaction,
            json=payload
        )

        # if is_test == "positive":
        #     assert self.check_response_is(HTTPStatus.OK)
        #     self.validate_transaction()
        # else:
        #     assert self.check_response_is(HTTPStatus.UNPROCESSABLE_ENTITY)