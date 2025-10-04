from http import HTTPStatus

import allure

from tests.api.services.transactions.get_all_transactions import GetAllTransactions


@allure.epic("API")
@allure.feature("Transaction")
@allure.story("GetAllTransactions")
class TestGetAllTransactions(GetAllTransactions):

    def test_get_all_transactions(self) -> None:
        self.get_all_transactions()
        assert self.check_response_is(HTTPStatus.OK)
        self.validate_list_of_transactions()
