## Описание
- Многоконтейнерное приложение на Python с центральным API-cервером на FastAPI.
- запус всего проекта (16 контейнеров) одной командой (докер композз)
- 60+ тестов с отчетом в Allure
- Каждый тип тестов "упакован" в свой докер-контейнер. 
- Тестовые данные генеритуются динамически с помощью Faker
- Логи в Kibana
- Метрики в Grafana (со старта контейнер создается с преднастроенным дашбордом). 

## 📁 Структура проекта
- `app/` — API сервер на FastAPI  
- `infra/` — инфраструктура (ELK, Grafana)
- `tests/`
  - `api/` — API тесты приложения с использованием Pytest, Requests и валидацией данных через Pydentic.
  - `ui/` — UI тесты стороннего ресурса (https://www.saucedemo.com/) с использованием Playwright
    - `sync/` — синхронные тесты. 1 тест "упадет" чтобы показать что в этом случае автоматически будет получен скриншот. 
    - `async/` — асинхронные тесты 
  - `performance/` — перформанс тесты приложения с применением Locust 
- `welcome-page/` — начальная страница (Flask) для удобной навигации по сервисам
- `docker-compose.yml` — основная конфигурация Docker Compose

## Схема проекта

![Описание изображения](https://raw.githubusercontent.com/K-Alex-N/assets/main/docker/main.png)





## 🚀 Быстрый старт

### Требования
- Установленный Docker

### Запуск
```bash
git clone https://github.com/K-Alex-N/api_python_fastapi.git
cd api_python_fastapi
docker compose up
```
### После запуска (16 контейнеров) 
welcome page -   
allure report - 

## еще несколько особенностей
- данные в контейнерах очищены с помоью .dockerignore и не копирования "всего вподряд".

[//]: # (image_on_github = "https://github.com/K-Alex-N/assets/main/docker/2025-07-04%2000_31_51-pet-project__docker.drawio%20-%20draw.io.png")
[//]: # (raw_image = image_on_github.replace&#40;"github", "raw.githubusercontent"&#41;)
[//]: # (Комментарий для докер-копоз файла)
[//]: # (https://1drv.ms/x/c/6399a0f415bd70c8/EbY4_7V1KEBIkaZc1B0_IKQB8T2xSWTXzQel6y8OXf-dwQ?e=PJ6eEC)








