from typing import Any

from faker import Faker

from tests.api.services.categories.get_all_categories import GetAllCategories
from tests.api.base_client import BaseClient

fake = Faker()


class Payloads:
    def __init__(self, client: BaseClient):
        self.client = client

    async def create_transaction(self) -> dict[str, Any]:
        get_all_categories = GetAllCategories(self.client)
        category_id = await get_all_categories.get_random_category_id()
        return {
            "amount": fake.pyint(min_value=10, max_value=2000),
            "date": str(fake.date_time_between(start_date="-30d")),
            "description": fake.sentence(),
            "category_id": category_id,
        }

    async def _modified_transaction(self, *, drop=None, overrides=None) -> dict[str, Any]:
        transaction = await self.create_transaction()
        if drop:
            for key in drop:
                transaction.pop(key, None)
        if overrides:
            transaction.update(overrides)
        return transaction

    async def create_transaction_without_amount(self) -> dict[str, Any]:
        return await self._modified_transaction(drop=["amount"])

    async def create_transaction_without_date(self) -> dict[str, Any]:
        return await self._modified_transaction(drop=["date"])

    async def create_transaction_without_description(self) -> dict[str, Any]:
        return await self._modified_transaction(drop=["description"])

    async def create_transaction_without_category_id(self) -> dict[str, Any]:
        return await self._modified_transaction(drop=["category_id"])

    async def create_transaction_with_wrong_amount(self) -> dict[str, Any]:
        return await self._modified_transaction(overrides={"amount": "some string"})

    async def create_transaction_with_wrong_date(self) -> dict[str, Any]:
        return await self._modified_transaction(overrides={"date": "wrong date"})

    async def create_transaction_with_wrong_description(self) -> dict[str, Any]:
        return await self._modified_transaction(overrides={"description": 12345})

    async def create_transaction_with_wrong_category_id(self) -> dict[str, Any]:
        return await self._modified_transaction(overrides={"category_id": 12345})
