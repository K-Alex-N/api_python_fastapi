from locust import HttpUser, between, task


class APIUser(HttpUser):
    wait_time = between(1, 3)

    @task(3)
    def get_transactions(self) -> None:
        self.client.get("/transactions")

    @task(1)
    def get_categories(self) -> None:
        self.client.get("/categories")


# в on_start добавить создание 100 объектов (чтобы случайна выборка из 100 работала)
# в on_stop чистить БД
