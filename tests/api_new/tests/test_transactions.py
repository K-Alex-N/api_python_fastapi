import pytest

from tests.api_new.services.transactions.api import TransactionsAPI


class TestTransactions(TransactionsAPI):

    # @pytest.mark.skip
    def test_create_transaction(self):
        self.create_transaction()

    @pytest.mark.skip
    def test_create_transaction_with_wrong_type(self):
        pass

    # @pytest.mark.skip
    def test_get_transaction_by_id(self):
        transaction = self.create_transaction()
        print(transaction)
        self.get_transaction_by_id(transaction.id)

    @pytest.mark.skip
    def test_get_transaction_by_wrong_id(self):
        pass

    # @pytest.mark.skip
    def test_get_all_transactions(self):
        self.create_transaction()
        self.get_all_transactions()

    @pytest.mark.skip
    def test_update_transaction(self):
        transaction = self.create_transaction()
        self.update_transaction(transaction.id)

    @pytest.mark.skip
    def test_delete_transaction(self):
        transaction = self.create_transaction()
        print("\n\n\n", transaction.id)
        self.delete_transaction(transaction.id)
