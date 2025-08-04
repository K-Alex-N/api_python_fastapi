FROM python:3.13-slim
ENV PYTHONUNBUFFERED=1

WORKDIR tests/api
ENV PYTHONPATH=tests/api

COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . .
#COPY . api/
COPY __init__.py ..

RUN chmod +x entrypoint.sh
CMD ["bash", "entrypoint.sh"]
#
#CMD ["pytest", "tests/api/tests/test_categories"]
#CMD ["pytest", "tests/api/tests/test_transactions"]
#CMD ["pytest"]
#CMD ["sleep", "infinity"]