from tests.api_new.common.config import BASE_URL


class URLs:
    CATEGORIES_URL = BASE_URL + '/categories/'

    create_category = CATEGORIES_URL
    get_all_categories = CATEGORIES_URL
    get_category_by_id = lambda self, _id: f"{self.CATEGORIES_URL}{_id}"
    update_category = lambda self, _id: f"{self.CATEGORIES_URL}{_id}"
    delete_category = lambda self, _id: f"{self.CATEGORIES_URL}{_id}"


url = URLs()
