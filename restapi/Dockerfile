FROM ubuntu:20.04

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

ENV REST_API=/home/app/restapi/

RUN apt-get update -y
RUN apt install software-properties-common -y
RUN apt-get install -y python3 python3-pip python3-dev python-setuptools

RUN mkdir -p $REST_API
RUN mkdir -p $REST_API/static

WORKDIR $REST_API

COPY . $REST_API

RUN pip install -r requirements.txt
