import pytest

from tests.api.services.categories.create_category import CreateCategory
from tests.api.services.categories.payloads import payloads
from tests.api.services.transactions.create_transaction import CreateTransaction
from tests.api.services.transactions.payloads import payloads as payload_trnx


@pytest.fixture(scope="session", autouse=True)
def prefill_db() -> None:
    number_of_categories = 3
    for _ in range(number_of_categories):
        CreateCategory().create_category(payloads.category())

    number_of_transactions = 3
    for _ in range(number_of_transactions):
        CreateTransaction().create_transaction(payload_trnx.create_transaction())
