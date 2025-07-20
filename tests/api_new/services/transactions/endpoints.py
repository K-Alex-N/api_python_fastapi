from tests.api_new.common.config import BASE_URL


class Endpoints:
    BASE_URL_TRANSACTIONS = BASE_URL + '/transactions/'

    create_transaction = BASE_URL_TRANSACTIONS
    get_all_transactions = BASE_URL_TRANSACTIONS
    get_transaction_by_id = lambda self, _id: f"{self.BASE_URL_TRANSACTIONS}{_id}"
    update_transaction = lambda self, _id: f"{self.BASE_URL_TRANSACTIONS}{_id}"
    delete_transaction = lambda self, _id: f"{self.BASE_URL_TRANSACTIONS}{_id}"


endpoints = Endpoints()
