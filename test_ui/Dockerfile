FROM python:3.11-slim

# Установка зависимостей
RUN apt-get update && apt-get install -y \
    curl \
    git \
    unzip \
    wget \
    && apt-get clean

WORKDIR /app

# Копируем файлы проекта
COPY . .

# Устанавливаем зависимости
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Устанавливаем Playwright и браузеры
RUN playwright install --with-deps

#RUN chmod +x /app/entrypoint.sh

# Делаем entrypoint исполняемым
RUN chmod +x /app/entrypoint.sh

#ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["bash", "/app/entrypoint.sh"]
