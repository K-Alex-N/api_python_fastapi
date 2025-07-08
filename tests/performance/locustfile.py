from locust import HttpUser, task, between

class APIUser(HttpUser):
    wait_time = between(1, 3)

    @task(3)
    def health(self):
        self.client.get("/health")

    @task
    def test_add(self):
        self.client.post("/test_add")


# в on_start добавить создание 100 объектов (чтобы случайна выборка из 100 работала)
# в on_stop чистить БД