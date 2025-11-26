from http import HTTPStatus

import allure
import pytest

from tests.api.services.transactions.create_transaction import CreateTransaction
from tests.api.services.transactions.delete_transaction import DeleteTransaction
from tests.api.services.transactions.payloads import Payloads


@allure.epic("API")
@allure.feature("Transaction")
@allure.story("DeleteTransaction")
@pytest.mark.asyncio(loop_scope="session")
class TestDeleteTransaction:
    async def test_delete_transaction_success(self, client) -> None:
        payloads = Payloads(client)
        create_transaction = CreateTransaction(client)
        delete_transaction = DeleteTransaction(client)

        # create a transactions
        await create_transaction.create_transaction(await payloads.create_transaction())
        transaction_id = create_transaction.response_json.get("id")
        assert await create_transaction.check_response_is(HTTPStatus.OK)

        # delete the transactions
        await delete_transaction.delete_transaction(transaction_id)

        # check the transactions was deleted
        assert await delete_transaction.check_response_is(HTTPStatus.OK)
        assert await delete_transaction.is_transaction_deleted(transaction_id)

    @pytest.mark.parametrize(
        "transaction_id",
        [
            "wrong id",
            12345,
        ],
    )
    async def test_delete_transaction_fails_with_wrong_transaction_id(
        self, client, transaction_id
    ) -> None:
        delete_transaction = DeleteTransaction(client)
        await delete_transaction.delete_transaction(transaction_id)

        assert await delete_transaction.check_response_is(HTTPStatus.UNPROCESSABLE_ENTITY)
