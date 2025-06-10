FROM python:3.13-alpine
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# COPY . .  - скопировать все из папки APP ??? - чтобы дергать какие то методы из main? - нетт
# COPY . .  - скопировать только models.py
CMD ["pytest", "--alluredir=allure-results"]
#CMD ["pytest", "-sv", "--alluredir=allure-results"]
