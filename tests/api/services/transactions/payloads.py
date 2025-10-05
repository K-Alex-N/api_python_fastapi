from faker import Faker

from tests.api.services.categories.get_all_categories import GetAllCategories

fake = Faker()


class Payloads:

    @staticmethod
    def create_transaction() -> dict:
        category_id = GetAllCategories().get_random_category_id()
        return {
            "amount": fake.pyint(min_value=10, max_value=2000),
            "date": str(fake.date_time_between(start_date="-30d")),
            "description": fake.sentence(),
            "category_id": category_id,
        }

    def _modified_transaction(self, *, drop=None, overrides=None) -> dict:
        transaction = self.create_transaction()
        if drop:
            for key in drop:
                transaction.pop(key, None)
        if overrides:
            transaction.update(overrides)
        return transaction

    def create_transaction_without_amount(self) -> dict:
        return self._modified_transaction(drop=["amount"])

    def create_transaction_without_date(self) -> dict:
        return self._modified_transaction(drop=["date"])

    def create_transaction_without_description(self) -> dict:
        return self._modified_transaction(drop=["description"])

    def create_transaction_without_category_id(self) -> dict:
        return self._modified_transaction(drop=["category_id"])

    def create_transaction_with_wrong_amount(self) -> dict:
        return self._modified_transaction(overrides={"amount": "some string"})

    def create_transaction_with_wrong_date(self) -> dict:
        return self._modified_transaction(overrides={"date": "wrong date"})

    def create_transaction_with_wrong_description(self) -> dict:
        return self._modified_transaction(overrides={"description": 12345})

    def create_transaction_with_wrong_category_id(self) -> dict:
        return self._modified_transaction(overrides={"category_id": 12345})


payloads = Payloads()
