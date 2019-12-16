FROM ubuntu:19.04

MAINTAINER Gregor von Laszewski <laszewski@gmail.com>

RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get -y --no-install-recommends install build-essential
RUN apt-get -y --no-install-recommends install git
RUN apt-get -y --no-install-recommends install curl
RUN apt-get -y --no-install-recommends install wget
RUN apt-get -y --no-install-recommends install sudo
RUN apt-get -y install python3
RUN apt-get -y install python3-pip

RUN ln -s /usr/bin/python3 /usr/bin/python
RUN ln -s /usr/bin/pip3 /usr/bin/pip

RUN apt-get -y --no-install-recommends install mongodb


RUN pip install cloudmesh-installer

RUN mkdir cm
WORKDIR cm

RUN ls
RUN echo
RUN cloudmesh-installer git clone cloud
RUN cloudmesh-installer install cloud -e

RUN apt-get update
RUN apt-get install -y python3-pip libmysqlclient-dev gcc libssl-dev libkrb5-dev vim dos2unix
# RUN pip3 install Flask==1.0.4
ENV AIRFLOW_HOME=/usr/local/airflow
RUN pip3 install apache-airflow

COPY /config/airflow.cfg /usr/local/airflow/airflow.cfg
COPY /script/entrypoint.sh /entrypoint.sh

RUN dos2unix /entrypoint.sh

RUN pip install -U pytest
