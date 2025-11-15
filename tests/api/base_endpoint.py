import json

import allure

from tests.api.base_client import BaseClient


class BaseEndpoint:
    def __init__(self, client: BaseClient):
        self.client = client
        self.response = None
        self.response_json = None

    @allure.step("Check response status code equal {status_code}")
    async def check_response_is(self, status_code: int) -> bool:
        return self.response.status_code == status_code

    async def allure_attach_response(self) -> None:
        allure.attach(
            json.dumps(self.response_json, indent=4),
            name="API Response",
            attachment_type=allure.attachment_type.JSON,
        )

    @staticmethod
    async def allure_attach_schema(schema) -> None:
        allure.attach(
            json.dumps(schema.model_json_schema(), indent=4),
            name="Validation schema",
            attachment_type=allure.attachment_type.JSON,
        )

    @allure.step("Validate response against schema {schema}")
    async def validate(self, schema) -> None:
        schema.model_validate(self.response_json)
        await self.allure_attach_schema(schema)

    async def process_response(self) -> None:
        self.response_json = self.response.json()
        await self.allure_attach_response()
