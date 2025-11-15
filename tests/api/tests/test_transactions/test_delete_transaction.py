from http import HTTPStatus

import allure
import pytest

from tests.api.services.transactions.delete_transaction import DeleteTransaction
from tests.api.services.transactions.get_all_transactions import GetAllTransactions


@allure.epic("API")
@allure.feature("Transaction")
@allure.story("DeleteTransaction")
@pytest.mark.asyncio(loop_scope="session")
class TestDeleteTransaction:
    async def test_delete_transaction_success(self, client) -> None:
        get_all_transactions = GetAllTransactions(client)
        delete_transaction = DeleteTransaction(client)
        
        transaction_id = await get_all_transactions.get_random_transaction_id()
        await delete_transaction.delete_transaction(transaction_id)

        assert await delete_transaction.check_response_is(HTTPStatus.OK)
        assert await delete_transaction.is_transaction_deleted(transaction_id)

    @pytest.mark.parametrize(
        "transaction_id",
        [
            "wrong id",
        ],
    )
    async def test_delete_transaction_fails(self, client, transaction_id) -> None:
        delete_transaction = DeleteTransaction(client)
        await delete_transaction.delete_transaction(transaction_id)

        assert await delete_transaction.check_response_is(HTTPStatus.UNPROCESSABLE_ENTITY)
