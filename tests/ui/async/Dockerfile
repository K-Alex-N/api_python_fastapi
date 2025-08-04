FROM python:3.13-slim
ENV PYTHONUNBUFFERED=1

WORKDIR tests
ENV PYTHONPATH=tests

COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

RUN playwright install chromium --with-deps

COPY __init__.py .
COPY . ui/async
COPY __init__.py ui

#RUN chmod +x entrypoint.sh
#CMD ["bash", "entrypoint.sh"]

CMD ["pytest"]