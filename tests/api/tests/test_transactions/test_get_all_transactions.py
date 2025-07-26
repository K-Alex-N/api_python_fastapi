from http import HTTPStatus

from tests.api.services.transactions.get_all_transactions import GetAllTransactions


class TestGetAllTransactions(GetAllTransactions):

    def test_get_all_transactions(self):
        self.get_all_transactions()
        assert self.check_response_is(HTTPStatus.OK)
        self.validate_list_of_transactions()
