class BaseTest:
    response = None
    response_json = None

    def check_response_is(self, status_code=200):
        return self.response.status_code == status_code
        # return self.response.status_code == status_code, self.response.json()
