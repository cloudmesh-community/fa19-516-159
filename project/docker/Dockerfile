# Download base image ubuntu 18.04
FROM ubuntu:18.04

MAINTAINER austin zebrowski

# Update ubuntu software

RUN apt-get update

# Install libraries

RUN apt-get install -y python3-pip libmysqlclient-dev gcc libssl-dev libkrb5-dev libsasl2-dev
RUN apt-get install vim -y
RUN pip3 install Flask==1.0.4

ENV AIRFLOW_HOME=/usr/local/airflow

RUN pip3 install apache-airflow

RUN apt-get install -y dos2unix

COPY /config/airflow.cfg /usr/local/airflow/airflow.cfg
COPY /script/entrypoint.sh /entrypoint.sh

# convert to unix format

RUN dos2unix /entrypoint.sh
