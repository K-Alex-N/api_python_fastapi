import pytest
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
            "category_id": category_id
        }

    def create_transaction_without_amount(self) -> dict:
        transaction = self.create_transaction()
        del transaction["amount"]
        return transaction

    def create_transaction_without_date(self) -> dict:
        transaction = self.create_transaction()
        del transaction["date"]
        return transaction

    def create_transaction_without_description(self) -> dict:
        transaction = self.create_transaction()
        del transaction["description"]
        return transaction

    def create_transaction_without_category_id(self) -> dict:
        transaction = self.create_transaction()
        del transaction["category_id"]
        return transaction

    def create_transaction_with_wrong_amount(self) -> dict:
        transaction = self.create_transaction()
        transaction["amount"] = "some string"
        return transaction

    def create_transaction_with_wrong_date(self) -> dict:
        transaction = self.create_transaction()
        transaction["date"] = "wrong date"
        return transaction

    def create_transaction_with_wrong_description(self) -> dict:
        transaction = self.create_transaction()
        transaction["description"] = 12345
        return transaction

    def create_transaction_with_wrong_category_id(self) -> dict:
        transaction = self.create_transaction()
        transaction["category_id"] = 12345
        return transaction


payloads = Payloads()
