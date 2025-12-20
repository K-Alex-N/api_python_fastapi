FROM python:3.13-slim
ENV PYTHONUNBUFFERED=1

# на относительных путях
WORKDIR tests/ui/sync

COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

RUN playwright install chromium --with-deps

COPY . .

CMD ["pytest"]