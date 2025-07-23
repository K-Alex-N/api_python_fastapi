from http import HTTPStatus

import pytest
import requests

from tests.api.services.transactions.api import TransactionsAPI
from tests.api.services.transactions.payloads import payloads
from tests.api.services.transactions.urls import url


class TestTransactions(TransactionsAPI):



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
