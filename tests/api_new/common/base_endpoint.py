import json

import allure
from allure_commons.types import AttachmentType


# from tests.api_new.common.helper import Helper


class BaseEndpoint():
    response = None
    response_json = None

    @allure.step("Check response status code equal {status_code}")
    def check_response_is(self, status_code=200):
        return self.response.status_code == status_code

    @staticmethod
    @allure.step("Attach response into allure")
    def attach_response(response):
        response = json.dumps(response, indent=4)
        allure.attach(body=response, name="API Response", attachment_type=AttachmentType.JSON)


    def _process_response(self):
        self.response_json = self.response.json()
        self.attach_response(self.response_json)