### Многоконтейнерное Python-приложение по учету личных финансов с RESTful API-сервисом, разработанным на FastAPI и MongoDB

![Описание изображения](https://raw.githubusercontent.com/K-Alex-N/assets/main/docker/main.png)

### 📄 Описание 
* **Тесты**
  * **60+** тестов.
  * Изоляция тестов: каждый тип тестов "упакован" в собственный контейнер. 
  * **UI тесты** (сайта https://www.saucedemo.com/) с sync и async версиями и применением Playwright.
     * Архитектура: Page Obdject + Page Elements.
     * "Упавшие" тесты для демонстрации автоматического добавления скриншота в Allur отчет
  * **API тесты** с использованием Pytest, Requests и валидацией данных через Pydentic.
    * Динамическая генерация тестовых данных (Faker)
  * **Перформанс тесты** приложения с помощью Locust
  * Результаты тестов в **Allure**-отчете:
    * c прикреплением json-схемы ответа (в API тестах) и скриншота (в UI тестах) 
    * c группировкой по epic, feature, story
    * c добавлением allure.steps для более быстрого анализа дефектов
* **Мониторинг и логирование**:
  * Логи в Kibana. 
  * Метрики в Grafana (контейнер создается с преднастроенным дашбордом). 
* **Docker**
  * **Запуск** всего проекта (16 контейнеров) **одной командой** (`docker compose up`). 
  * "Чистые" контейнеры (копируется только нужные файлы, ненужное очищается с помощью .dockerignore)
* **Мониторинг и логирование:**
  * Логи — в **Kibana**
  * Метрики — в **Grafana** (контейнер создается с преднастроенным дашбордом). 
* **"Welcome page"** на Flask — удобная точка входа ко всем сервисам



### 🚀 Быстрый старт

**Требования**: установлен Docker

**Запуск**  
Склонируйте репозиторий
```bash
git clone https://github.com/K-Alex-N/api_python_fastapi.git
cd api_python_fastapi
```
Запустите команду
```bash
docker compose up
```
**Результат**  
Allure report: http://localhost:5050/allure-docker-service/projects/default/reports/latest/index.html  
Welcome page: http://localhost:5000


### 📈 Планы на развитие:
- Расширение API-сервера (больше "ручек")
- Работа с очередями RabbitMQ/Kafka
- Расширение тестов, расширение UI фрэймворка (добавить Page Components) 
- Перенос результатов тестов из Allure в Grafana
  
  
![Docker](https://img.shields.io/badge/Docker-ready-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-v0.100+-green)
![Python](https://img.shields.io/badge/Python-3.11+-blue)

