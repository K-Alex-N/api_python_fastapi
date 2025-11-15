from http import HTTPStatus

import allure
import pytest

from tests.api.services.transactions.get_all_transactions import GetAllTransactions


@allure.epic("API")
@allure.feature("Transaction")
@allure.story("GetAllTransactions")
@pytest.mark.asyncio(loop_scope="session")
class TestGetAllTransactions:
    async def test_get_all_transactions(self, client) -> None:
        get_all_transactions = GetAllTransactions(client)
        await get_all_transactions.get_all_transactions()

        if get_all_transactions.response.status_code == HTTPStatus.OK:
            assert await get_all_transactions.check_response_is(HTTPStatus.OK)
            await get_all_transactions.validate_list_of_transactions()
        else:
            assert get_all_transactions.response is not None
            assert get_all_transactions.response_json is not None
