from flask import Flask, render_template

app = Flask(__name__)

services_list = [
    ("Основное", "", ""),
    ("Kibana", "5601", "Чтобы начал показывать логи нужно индекс прописать..."),
    ("API (Swagger)", "8000/docs",
     "Свагер. АПИшки наделаны под каждый сервис. Какой то логики и смысла там нет. Ничего интересного."),
    ("GUI MongoDB", "8081", "Mongo Express - графический интерфейс для MongoDB"),
    ("Locast", "8089",
     "можно перформанс запустить. Выбрать Виртуальных пользователей, ... и время например 30 (это будут секунды)"),
    ("Grafana", "3000", "логин admin, пароль admin. В следующем окне жмем Skip."),

    ("М.б. тоже интересно будет", "", ""),
    ("Elasticsearch", "9200", "Будет маленький Json'чик с информацией об Эластике"),
    ("Grafana", "3000", "логин admin, пароль admin. Затем Skip нажать надо. Шаблон простой сделал. "),
    ("Allure", "5050/allure-docker-service/projects/default/reports/latest/index.html",
     "Покажет результаты всех тестов (sync/async, UI/API). Некоторые тесты упавшие, это специально чтобы покаать что там скриншот будет делаться.  "),

    ("Prometheus", "9090", "??? чего тут смотреть"),

]

image_on_github = "https://github.com/K-Alex-N/assets/main/docker/2025-07-04%2000_31_51-pet-project__docker.drawio%20-%20draw.io.png"
raw_image = image_on_github.replace("github", "raw.githubusercontent")


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
