FROM python:3.5.1-alpine
ADD . /var/www/project
WORKDIR /var/www/project
RUN apk add --no-cache git
RUN pip install --no-cache-dir -r requirements.txt
