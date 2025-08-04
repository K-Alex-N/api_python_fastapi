FROM python:3.13-slim
ENV PYTHONUNBUFFERED=1

WORKDIR tests/ui/async

COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

RUN playwright install chromium --with-deps

COPY . .
COPY __init__.py ..
COPY __init__.py ...

CMD ["pytest"]