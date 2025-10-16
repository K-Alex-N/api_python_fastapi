from locust import HttpUser, between, task

from tests.api.services.transactions.payloads import payloads as transactions_payloads
from tests.api.tests.test_categories.test_create_category import TestCreateCategory
from tests.api.tests.test_transactions.test_create_transaction import (
    TestCreateTransaction,
)


class APIUser(HttpUser):
    wait_time = between(1, 3)

    def on_start(self):
        categories_number = 10
        transactions_number = 30

        for _ in range(categories_number):
            TestCreateCategory().test_create_category_success()

        for _ in range(transactions_number):
            TestCreateTransaction().test_create_transaction(
                "positive", transactions_payloads.create_transaction
            )

    @task(1)
    def get_categories(self) -> None:
        self.client.get("/categories")

    @task(3)
    def get_transactions(self) -> None:
        self.client.get("/transactions")
