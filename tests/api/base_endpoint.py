import json

import allure


class BaseEndpoint:
    response = None
    response_json = None

    @allure.step("Check response status code equal {status_code}")
    def check_response_is(self, status_code=200):
        return self.response.status_code == status_code

    @staticmethod
    def allure_attach_response(response):
        allure.attach(
            json.dumps(response, indent=4),
            name="API Response",
            attachment_type=allure.attachment_type.JSON
        )

    @staticmethod
    def allure_attach_schema(schema):
        allure.attach(
            json.dumps(schema.model_json_schema(), indent=4),
            name="Validation schema",
            attachment_type=allure.attachment_type.JSON
        )

    @allure.step("Validate response against schema {schema}")
    def validate(self, schema):
        schema.model_validate(self.response_json)
        self.allure_attach_schema(schema)

    def _process_response(self):
        self.response_json = self.response.json()
        self.allure_attach_response(self.response_json)
