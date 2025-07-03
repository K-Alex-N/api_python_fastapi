FROM python:3.13-slim
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install locust # можно и без requirements.txt

COPY locustfile.py .

EXPOSE 8089

CMD ["locust", "-f", "locustfile.py", "--host", "http://api:8000"]