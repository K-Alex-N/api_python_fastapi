FROM python:3.11-slim

WORKDIR /welcome

COPY . .

RUN pip install flask

EXPOSE 5000

CMD ["python", "main.py"]
