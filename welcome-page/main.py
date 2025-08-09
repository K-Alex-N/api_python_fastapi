from flask import Flask, render_template

app = Flask(__name__)
services_list = [
    ("Allure", "5050/allure-docker-service/projects/default/reports/latest/index.html",
     "Результаты всех тестов (UI/API). Пара тестов \"упадет\" для демонстрации автоматического прикрепления скриншота"),
    ("API (Swagger)", "8000/docs",
     "Свагер. АПИшки наделаны под каждый сервис. Какой то логики и смысла там нет. Ничего интересного."),
    ("Locust", "8089",
     "Перформанс тест. Для запуска нужно выбрать количество виртуальных пользователей (например 500), скорость добавления пользователей в секунду (например 50) и длительность теста (например 30  - это будут секунды)"),
    ("Grafana", "3000",
     "Логин admin, пароль admin. В следующем окне жмем Skip. Выбрать предустановленный дашборд. Данные начнуть \"шевелиться\" если locust запустить или ручки в свагере подергать."),
    ("Kibana", "5601", "Чтобы начал показывать логи нужно индекс прописать..."),
    ("GUI MongoDB", "8081", "Mongo Express - графический интерфейс для MongoDB"),
    # ("Elasticsearch", "9200", "Будет маленький Json'чик с информацией об Эластике"),
    # ("Prometheus", "9090", "??? чего тут смотреть"),

]

raw_image = "https://raw.githubusercontent.com/K-Alex-N/assets/main/docker/main.png"


@app.route("/")
def index():
    services = []
    for service_name, endpoint, comment in services_list:
        services.append({
            "name": service_name,
            "url": f"http://localhost:{endpoint}",
            "comment": comment
        })

    return render_template("index.html", services=services, image=raw_image)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
