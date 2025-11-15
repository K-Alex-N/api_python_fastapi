import allure
import httpx


class BaseClient:
    def __init__(self, headers: dict | None = None):
        self.headers = headers or {}

    async def _send_request(self, method: str, url: str, **kwargs) -> httpx.Response:
        async with httpx.AsyncClient(headers=self.headers) as client:
            response = await client.request(method, url, **kwargs)
            allure.attach(
                response.text, f"{method} {url} response", allure.attachment_type.TEXT
            )
            return response

    @allure.step("Send GET request to {url}")
    async def get(self, url: str, **kwargs) -> httpx.Response:
        return await self._send_request("GET", url, **kwargs)

    @allure.step("Send POST request to {url}")
    async def post(self, url: str, **kwargs) -> httpx.Response:
        return await self._send_request("POST", url, **kwargs)

    @allure.step("Send PUT request to {url}")
    async def put(self, url: str, **kwargs) -> httpx.Response:
        return await self._send_request("PUT", url, **kwargs)

    @allure.step("Send DELETE request to {url}")
    async def delete(self, url: str, **kwargs) -> httpx.Response:
        return await self._send_request("DELETE", url, **kwargs)

    @allure.step("Send PATCH request to {url}")
    async def patch(self, url: str, **kwargs) -> httpx.Response:
        return await self._send_request("PATCH", url, **kwargs)
