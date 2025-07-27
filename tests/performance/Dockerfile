FROM python:3.13-slim
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install locust==2.37.11 # можно и без requirements.txt

COPY locustfile.py .

EXPOSE 8089

ENTRYPOINT ["locust", "-f", "locustfile.py"]
CMD ["--host", "http://api:8000"]