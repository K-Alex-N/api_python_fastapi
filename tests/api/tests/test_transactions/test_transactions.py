import pytest

from tests.api.services.transactions.api import TransactionsAPI


class TestTransactions(TransactionsAPI):

    def test_create_transaction(self):
        self.create_transaction()

    def test_get_transaction_by_id(self):
        transaction = self.create_transaction()
        self.get_transaction_by_id(transaction.id)

    def test_get_all_transactions(self):
        self.create_transaction()
        self.get_all_transactions()

    def test_update_transaction(self):
        transaction = self.create_transaction()
        self.update_transaction(transaction.id)

    def test_delete_transaction(self):
        transaction = self.create_transaction()
        self.delete_transaction(transaction.id)
