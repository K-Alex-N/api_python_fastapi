FROM python:3.13-alpine
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apk add --no-cache curl # для хэлфсчека нужно
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
