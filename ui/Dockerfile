FROM ubuntu:20.04

ENV UI=/home/app/ui/

RUN apt-get update -y
RUN apt install nodejs -y
RUN apt install npm -y

RUN mkdir -p $UI

WORKDIR $UI

COPY . $UI
