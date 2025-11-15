from http import HTTPStatus

import allure
import pytest

from tests.api.services.transactions.create_transaction import CreateTransaction
from tests.api.services.transactions.payloads import Payloads


@allure.epic("API")
@allure.feature("Transaction")
@allure.story("CreateTransaction")
@pytest.mark.asyncio(loop_scope="session")
class TestCreateTransaction:
    async def test_create_transaction_success(self, client) -> None:
        payloads = Payloads(client)
        create_transaction = CreateTransaction(client)
        
        await create_transaction.create_transaction(await payloads.create_transaction())
        assert await create_transaction.check_response_is(HTTPStatus.OK)
        await create_transaction.validate_transaction()

    @pytest.mark.parametrize(
        "payload_method",
        [
            "create_transaction_without_amount",
            "create_transaction_without_date", 
            "create_transaction_without_description",
            "create_transaction_without_category_id",
            "create_transaction_with_wrong_amount",
            "create_transaction_with_wrong_date",
            "create_transaction_with_wrong_description",
            "create_transaction_with_wrong_category_id",
        ],
    )
    async def test_create_transaction_fails(self, client, payload_method) -> None:
        payloads = Payloads(client)
        create_transaction = CreateTransaction(client)
        
        payload = await getattr(payloads, payload_method)()
        await create_transaction.create_transaction(payload)
        assert await create_transaction.check_response_is(HTTPStatus.UNPROCESSABLE_ENTITY)
