
[//]: # (## Содержание)

[//]: # (* [Установка]&#40;#установка&#41;)

[//]: # (* [Начало работы]&#40;#начало-работы&#41;)

[//]: # (* [Документация API]&#40;#документация-api&#41;)

[//]: # (* [Тестирование]&#40;#тестирование&#41;)

[//]: # (* [Требования]&#40;#требования&#41;)

## 📄 Описание
Многоконтейнерное Python-приложение с центральным RESTful API-сервисом, разработанным на FastAPI.
- Запуск всего проекта (16 контейнеров) одной командой (`docker compose up`).
- 60+ тестов с отчетом в Allure
- Каждый тип тестов "упакован" в отдельный докер-контейнер. 
- API тесты с использованием Pytest, Requests и валидацию данных через Pydentic.
- UI тесты в синхронной и асинхронной версии с использованием Playwright
- Тестовые данные генеритуются динамически с помощью Faker
- В Allure отчет составлен с разделение на feature...
- с добавлением шагов для более быстрого анализа дефектов
- в отчет прикрепляются скриншоты при падении (UI тесты) и json-схемы ответов (API тесты) 
- Перформанс тесты приложения с применением Locust
- Логи в Kibana. Метрики в Grafana (контейнер создается с преднастроенным дашбордом). 
- Для удобной навигации по сервисам, добавлена "приветственная страница" (Flask)

[//]: # (POM, Elements)
[//]: # ()
## 📁 Структура проекта
- `app/` — API сервер (FastAPI)  
- `infra/` — инфраструктура (ELK, Grafana)
- `tests/`
  - `api/` — API тесты приложения (app/)
  - `performance/` — перформанс тесты приложения
  - `ui/` — UI тесты стороннего ресурса (https://www.saucedemo.com/)
    - `sync/` — синхронные тесты. 1 тест "упадет" для демонстрации автоматического получения скриншота. 
    - `async/` — асинхронные тесты 


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
Запустите
```bash
docker compose up
```
**Будут доступны**  
Welcome page:      
Allure report:  
Документация API (swagger):   


[//]: # (## еще несколько особенностей)

[//]: # (-)

[//]: # (- данные в контейнерах очищены с помоью .dockerignore и не копирования "всего вподряд".)

[//]: # (image_on_github = "https://github.com/K-Alex-N/assets/main/docker/2025-07-04%2000_31_51-pet-project__docker.drawio%20-%20draw.io.png")
[//]: # (raw_image = image_on_github.replace&#40;"github", "raw.githubusercontent"&#41;)
[//]: # (Комментарий для докер-копоз файла)
[//]: # (https://1drv.ms/x/c/6399a0f415bd70c8/EbY4_7V1KEBIkaZc1B0_IKQB8T2xSWTXzQel6y8OXf-dwQ?e=PJ6eEC)


## 📈 Планы на развитие:
- Расширение API-сервера (больше "ручек" добавить)
- Расширение тестов, добавить Page Components в UI фрэймворк
- Работа с очередями RabbitMQ/Kafka
- Перенос результатов тестов из Allure в Grafana
  
  
![Docker](https://img.shields.io/badge/Docker-ready-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-v0.100+-green)
![Python](https://img.shields.io/badge/Python-3.11+-blue)

