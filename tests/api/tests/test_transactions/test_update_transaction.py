from collections.abc import Callable
from http import HTTPStatus

import allure
import pytest

from tests.api.services.transactions.get_all_transactions import GetAllTransactions
from tests.api.services.transactions.payloads import Payloads
from tests.api.services.transactions.update_transaction import UpdateTransaction


@allure.epic("API")
@allure.feature("Transaction")
@allure.story("UpdateTransaction")
@pytest.mark.asyncio(loop_scope="session")
class TestUpdateTransaction:
    @pytest.mark.parametrize(
        "payload_method",
        [
            "create_transaction",
            "create_transaction_without_amount",
            "create_transaction_without_date",
            "create_transaction_without_description",
            "create_transaction_without_category_id",
        ],
    )
    async def test_update_transaction_success(self, client, payload_method) -> None:
        payloads = Payloads(client)
        get_all_transactions = GetAllTransactions(client)
        update_transaction = UpdateTransaction(client)
        
        transaction_id = await get_all_transactions.get_random_transaction_id()
        payload = await getattr(payloads, payload_method)()
        await update_transaction.update_transaction(transaction_id, payload)

        assert await update_transaction.check_response_is(HTTPStatus.OK)
        await update_transaction.validate_transaction()

    @pytest.mark.parametrize(
        "transaction_id, payload_method",
        [
            ("placeholder id", "create_transaction_with_wrong_amount"),
            ("placeholder id", "create_transaction_with_wrong_date"),
            ("placeholder id", "create_transaction_with_wrong_description"),
            ("placeholder id", "create_transaction_with_wrong_category_id"),
            ("wrong id", "create_transaction"),
            (12345678, "create_transaction"),
        ],
    )
    async def test_update_transaction_fails(self, client, transaction_id, payload_method) -> None:
        payloads = Payloads(client)
        get_all_transactions = GetAllTransactions(client)
        update_transaction = UpdateTransaction(client)
        
        if transaction_id == "placeholder id":
            transaction_id = await get_all_transactions.get_random_transaction_id()

        payload = await getattr(payloads, payload_method)()
        await update_transaction.update_transaction(transaction_id, payload)

        assert await update_transaction.check_response_is(HTTPStatus.UNPROCESSABLE_ENTITY)
