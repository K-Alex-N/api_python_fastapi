FROM python:3.13-alpine
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
#RUN apk update && apk add --no-cache bash
CMD ["pytest", "--alluredir=allure-results"]
#CMD ["pytest", "-sv", "--alluredir=allure-results"]
#CMD ["bash"]
