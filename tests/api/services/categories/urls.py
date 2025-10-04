from tests.api.config import BASE_URL


class URLs:
    CATEGORIES_URL = BASE_URL + "/categories/"

    create_category = CATEGORIES_URL
    get_all_categories = CATEGORIES_URL

    def get_category_by_id(self, _id) -> str:
        return f"{self.CATEGORIES_URL}{_id}"

    def update_category(self, _id) -> str:
        return f"{self.CATEGORIES_URL}{_id}"

    def delete_category(self, _id) -> str:
        return f"{self.CATEGORIES_URL}{_id}"


url = URLs()
