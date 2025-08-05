from app.api.transactions.schemas import TransactionOut, TransactionOutList
from tests.api.base_endpoint import BaseEndpoint


class TransactionEndpoint(BaseEndpoint):

    def validate_transaction(self):
        self.validate(TransactionOut)

    def validate_list_of_transactions(self):
        self.validate(TransactionOutList)
