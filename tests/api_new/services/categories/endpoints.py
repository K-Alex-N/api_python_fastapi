from tests.api_new.common.config import BASE_URL


class Endpoints:
    BASE_URL_CATEGORIES = BASE_URL + '/categories/'

    create_category = BASE_URL_CATEGORIES
    get_all_categories = BASE_URL_CATEGORIES
    get_category_by_id = lambda self, _id: f"{self.BASE_URL_CATEGORIES}{_id}"
    update_category = lambda self, _id: f"{self.BASE_URL_CATEGORIES}{_id}"
    delete_category = lambda self, _id: f"{self.BASE_URL_CATEGORIES}{_id}"


endpoints = Endpoints()
