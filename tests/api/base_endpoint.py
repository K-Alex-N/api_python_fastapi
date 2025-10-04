import json

import allure


class BaseEndpoint:
    response = None
    response_json = None

    @allure.step("Check response status code equal {status_code}")
    def check_response_is(self, status_code: int = 200) -> bool:
        return self.response.status_code == status_code

    def allure_attach_response(self) -> None:
        allure.attach(
            json.dumps(self.response_json, indent=4),
            name="API Response",
            attachment_type=allure.attachment_type.JSON,
        )

    @staticmethod
    def allure_attach_schema(schema) -> None:
        allure.attach(
            json.dumps(schema.model_json_schema(), indent=4),
            name="Validation schema",
            attachment_type=allure.attachment_type.JSON,
        )

    @allure.step("Validate response against schema {schema}")
    def validate(self, schema) -> None:
        schema.model_validate(self.response_json)
        self.allure_attach_schema(schema)

    def process_response(self) -> None:
        self.response_json = self.response.json()
        self.allure_attach_response()
