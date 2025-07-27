FROM python:3.11-slim

WORKDIR /welcome

COPY . .

RUN pip install Flask==3.1.1

EXPOSE 5000

CMD ["python", "main.py"]
