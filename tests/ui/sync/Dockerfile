FROM python:3.13-slim
ENV PYTHONUNBUFFERED=1

ARG BUILD_WORKDIR=test_ui
WORKDIR /${BUILD_WORKDIR}
ENV PYTHONPATH=/${BUILD_WORKDIR}

RUN apt-get update && apt-get install -y \
    curl \
    git \
    unzip \
    wget \
    && apt-get clean

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

RUN playwright install chromium --with-deps

COPY . .

RUN chmod +x entrypoint.sh
CMD ["bash", "entrypoint.sh"]
