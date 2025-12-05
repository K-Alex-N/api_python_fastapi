from http import HTTPStatus

import allure
import pytest

from tests.api.services.transactions.get_all_transactions import GetAllTransactions


@allure.epic("API")
@allure.feature("Transaction")
@allure.story("GetAllTransactions")
@pytest.mark.asyncio(loop_scope="session")
class TestGetAllTransactions:
    async def test_get_all_transactions(self, client):
        get_all_transactions = GetAllTransactions(client)
        await get_all_transactions.get_all_transactions()

        assert await get_all_transactions.check_response_is(HTTPStatus.OK)
        await get_all_transactions.validate_list_of_transactions()
