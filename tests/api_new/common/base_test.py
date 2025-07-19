from tests.api_new.services.categories.api import CategoriesAPI


class BaseTest:

    def setup_method(self):
        self.api = CategoriesAPI()