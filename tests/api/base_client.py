import allure
import requests


class BaseClient:
    def __init__(self, headers: dict | None = None):
        self.session = requests.Session()
        if headers:
            self.session.headers.update(headers)

    def _send_request(self, method: str, url: str, **kwargs) -> requests.Response:
        response = self.session.request(method, url, **kwargs)
        allure.attach(
            response.text, f"{method} {url} response", allure.attachment_type.TEXT
        )
        return response

    @allure.step("Send GET request to {url}")
    def get(self, url: str, **kwargs) -> requests.Response:
        return self._send_request("GET", url, **kwargs)

    @allure.step("Send POST request to {url}")
    def post(self, url: str, **kwargs) -> requests.Response:
        return self._send_request("POST", url, **kwargs)

    @allure.step("Send PUT request to {url}")
    def put(self, url: str, **kwargs) -> requests.Response:
        return self._send_request("PUT", url, **kwargs)

    @allure.step("Send PATCH request to {url}")
    def patch(self, url: str, **kwargs) -> requests.Response:
        return self._send_request("PATCH", url, **kwargs)

    @allure.step("Send DELETE request to {url}")
    def delete(self, url: str, **kwargs) -> requests.Response:
        return self._send_request("DELETE", url, **kwargs)
