import allure
import requests


class BaseClient:
    # def __init__(self, base_url: str, headers: dict | None = None):
    #     self.base_url = base_url.rstrip("/")
    #     self.session = requests.Session()
    #     if headers:
    #         self.session.headers.update(headers)

    @allure.step("Send GET request to {endpoint}")
    def get(self, endpoint: str, **kwargs) -> requests.Response:
        return self._send_request("GET", endpoint, **kwargs)

    @allure.step("Send POST request to {endpoint}")
    def post(self, endpoint: str, **kwargs) -> requests.Response:
        return self._send_request("POST", endpoint, **kwargs)

    @allure.step("Send PUT request to {endpoint}")
    def put(self, endpoint: str, **kwargs) -> requests.Response:
        return self._send_request("PUT", endpoint, **kwargs)

    @allure.step("Send DELETE request to {endpoint}")
    def delete(self, endpoint: str, **kwargs) -> requests.Response:
        return self._send_request("DELETE", endpoint, **kwargs)

    def _send_request(self, method: str, endpoint: str, **kwargs) -> requests.Response:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = self.session.request(method, url, **kwargs)
        allure.attach(
            response.text, f"{method} {url} response", allure.attachment_type.TEXT
        )
        return response
