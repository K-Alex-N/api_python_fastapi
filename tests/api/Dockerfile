FROM python:3.13-slim
ENV PYTHONUNBUFFERED=1

#ARG BUILD_WORKDIR=test_api
#WORKDIR /${BUILD_WORKDIR}
#ENV PYTHONPATH=/${BUILD_WORKDIR}

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . tests/api/
COPY __init__.py tests

#RUN chmod +x test/api/entrypoint.sh
#CMD ["bash", "test/api/entrypoint.sh"]
#
CMD ["pytest", "tests"]
#CMD ["sleep", "infinity"]