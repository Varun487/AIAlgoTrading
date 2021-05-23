FROM ubuntu:20.04

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

ENV MICRO_SERVICE=/home/app/microservice

RUN apt-get update -y
RUN apt install software-properties-common -y
RUN apt-get install -y python3 python3-pip python3-dev python-setuptools cron

RUN mkdir -p $MICRO_SERVICE
RUN mkdir -p $MICRO_SERVICE/static

COPY cron/container_cronjob /etc/cron.d/container_cronjob
RUN chmod 0644 /etc/cron.d/container_cronjob
RUN crontab /etc/cron.d/container_cronjob

WORKDIR $MICRO_SERVICE

COPY . $MICRO_SERVICE

RUN pip install -r requirements.txt
