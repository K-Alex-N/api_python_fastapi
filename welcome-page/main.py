from flask import Flask, render_template

app = Flask(__name__)

services_list = [
    ("Kibana", "5601", "Нужно индекс прописать..."),
    ("API (Swagger)", "8000/docs",
     "Свагер. АПИшки наделаны под каждый сервис. Какой то логики и смысла там нет. Ничего интересного."),
    ("GUI MongoDB", "8081", "Графический интерфейс для Монго"),
    ("Elasticsearch", "9200", "Будет маленький Json'чик с информацией об Эластике"),
    ("Grafana", "3000", "логин admin, пароль admin. За"),
    ("", "", ""),
]


@app.route("/")
def index():
    services = []
    for service_name, endpoint, comment in services_list:
        services.append({
            "name": service_name,
            "url": f"http://localhost:{endpoint}",
            "comment": comment
        })

    return render_template("index.html", services=services)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
