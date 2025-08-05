
[//]: # (## Содержание)

[//]: # (* [Установка]&#40;#установка&#41;)

[//]: # (* [Начало работы]&#40;#начало-работы&#41;)

[//]: # (* [Документация API]&#40;#документация-api&#41;)

[//]: # (* [Тестирование]&#40;#тестирование&#41;)

[//]: # (* [Требования]&#40;#требования&#41;)

## 📄 Описание
**Многоконтейнерное Python-приложение по учету личных финансов с центральным RESTful API-сервисом, разработанным на FastAPI и MongoDB**
 
* **Тесты**
  * 60+ тестов.
  * Изоляция тестов: каждый тип тестов "упакован" в собственный контейнер. 
  * **UI тесты (Playwright)** стороннего ресурса (https://www.saucedemo.com/) с sync и async версиями.
     * Архитектура: POM со слоем Elements.
     * "Упавшие" тесты для демонстрации автоматического добавления скриншота в Allur отчет
  * **API тесты** с использованием Pytest, Requests и валидацией данных через Pydentic.
    * Тестовые данные генеритуются динамически с помощью Faker
  * Перформанс тесты приложения с помощью Locust
  * Результаты тестов в **Allure**: 
    * c группировкой по epic, feature, story
    * c добавлением allure.steps для более быстрого анализа дефектов
    * c добавлением скриншота при падении (UI тесты) и json-схемы ответа (API тесты) 
* **Мониторинг и логирование**:
  * Логи в Kibana. 
  * Метрики в Grafana (контейнер создается с преднастроенным дашбордом). 
* **Docker**
  * **Запуск всего проекта (16 контейнеров) одной командой** (`docker compose up`). 
  * контейнеры без лишних файлов (копируется только нужное и очищается с помощью .dockerignore)
* **Мониторинг и логирование:**
  * Логи — в Kibana
  * Метрики — в Grafana (контейнер создается с преднастроенным дашбордом). 
* **"Приветственная страница"**
  * Для удобной навигации по сервисам, добавлено мини-приложение на Flask.

## 🧩 Схема проекта

![Описание изображения](https://raw.githubusercontent.com/K-Alex-N/assets/main/docker/main.png)


## 🚀 Быстрый старт

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


[//]: # (## еще несколько особенностей)

[//]: # (-)

[//]: # (- данные в контейнерах очищены с помоью .dockerignore и не копирования "всего вподряд".)

[//]: # (image_on_github = "https://github.com/K-Alex-N/assets/main/docker/2025-07-04%2000_31_51-pet-project__docker.drawio%20-%20draw.io.png")
[//]: # (raw_image = image_on_github.replace&#40;"github", "raw.githubusercontent"&#41;)
[//]: # (Комментарий для докер-копоз файла)
[//]: # (https://1drv.ms/x/c/6399a0f415bd70c8/EbY4_7V1KEBIkaZc1B0_IKQB8T2xSWTXzQel6y8OXf-dwQ?e=PJ6eEC)


## 📈 Планы на развитие:
- Расширение API-сервера (больше "ручек")
- Работа с очередями RabbitMQ/Kafka
- Расширение тестов, расширение UI фрэймворка (добавить Page Components) 
- Перенос результатов тестов из Allure в Grafana
  
  
![Docker](https://img.shields.io/badge/Docker-ready-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-v0.100+-green)
![Python](https://img.shields.io/badge/Python-3.11+-blue)

