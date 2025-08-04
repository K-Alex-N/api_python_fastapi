FROM python:3.13-slim
ENV PYTHONUNBUFFERED=1

WORKDIR tests/ui/sync
ENV PYTHONPATH=tests/ui/sync

RUN apt-get update && apt-get install -y \
    curl \
    git \
    unzip \
    wget \
    && apt-get clean

COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

RUN playwright install chromium --with-deps


COPY . .
COPY __init__.py ..
COPY __init__.py ...

#RUN chmod +x tests/ui/sync/entrypoint.sh
#CMD ["bash", "tests/ui/sync/entrypoint.sh"]
#
CMD ["pytest"]