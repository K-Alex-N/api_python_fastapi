FROM python:3.13-slim
ENV PYTHONUNBUFFERED=1

#на абсолютных путях
WORKDIR tests/api

COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . .
COPY __init__.py ..

RUN chmod +x entrypoint.sh
CMD ["bash", "entrypoint.sh"]
