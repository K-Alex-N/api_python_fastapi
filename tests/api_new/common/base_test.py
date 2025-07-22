# from tests.api_new.services.categories.api import CategoriesAPI
#
#
class BaseTest:
    response = None

    # cat = CategoriesAPI()

    # @staticmethod
    # def setup_method(self):
    #     self.api = CategoriesAPI()

    def check_response_is(self, status_code=200):
        return self.response.status_code == status_code
        # return self.response.status_code == status_code, self.response.json()
