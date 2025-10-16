import json

import allure


class BaseEndpoint:
    response = None
    response_json = None

    @allure.step("Check response status code equal {status_code}")
    def check_response_is(self, status_code: int) -> bool:
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


# class BaseClient:
#     def __init__(self, base_url: str, headers: dict | None = None):
#         self.base_url = base_url.rstrip("/")
#         self.session = requests.Session()
#         if headers:
#             self.session.headers.update(headers)
#
#     @allure.step("Send GET request to {endpoint}")
#     def get(self, endpoint: str, **kwargs) -> requests.Response:
#         return self._send_request("GET", endpoint, **kwargs)
#
#     @allure.step("Send POST request to {endpoint}")
#     def post(self, endpoint: str, **kwargs) -> requests.Response:
#         return self._send_request("POST", endpoint, **kwargs)
#
#     @allure.step("Send PUT request to {endpoint}")
#     def put(self, endpoint: str, **kwargs) -> requests.Response:
#         return self._send_request("PUT", endpoint, **kwargs)
#
#     @allure.step("Send DELETE request to {endpoint}")
#     def delete(self, endpoint: str, **kwargs) -> requests.Response:
#         return self._send_request("DELETE", endpoint, **kwargs)
#
#     def _send_request(
#               self, method: str, endpoint: str, **kwargs) -> requests.Response:
#         url = f"{self.base_url}/{endpoint.lstrip('/')}"
#         response = self.session.request(method, url, **kwargs)
#         allure.attach(response.text,
#                       f"{method} {url} response", allure.attachment_type.TEXT)
#         return response
