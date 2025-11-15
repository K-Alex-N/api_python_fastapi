from http import HTTPStatus

import allure
import pytest

from tests.api.services.transactions.get_all_transactions import GetAllTransactions
from tests.api.services.transactions.get_transaction import GetTransaction


@allure.epic("API")
@allure.feature("Transaction")
@allure.story("GetTransaction")
@pytest.mark.asyncio(loop_scope="session")
class TestGetTransaction:
    async def test_get_transaction_by_id_success(self, client) -> None:
        get_all_transactions = GetAllTransactions(client)
        get_transaction = GetTransaction(client)
        
        transaction_id = await get_all_transactions.get_random_transaction_id()
        await get_transaction.get_transaction_by_id(transaction_id)

        assert await get_transaction.check_response_is(HTTPStatus.OK)
        await get_transaction.validate_transaction()

    @pytest.mark.parametrize(
        "transaction_id",
        [
            "wrong id",
            12345678,
        ],
    )
    async def test_get_transaction_by_id_fails(self, client, transaction_id) -> None:
        get_transaction = GetTransaction(client)
        await get_transaction.get_transaction_by_id(transaction_id)

        assert await get_transaction.check_response_is(HTTPStatus.UNPROCESSABLE_ENTITY)
