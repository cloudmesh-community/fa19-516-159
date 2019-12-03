FROM ubuntu:19.04

RUN set -x \
        && apt-get -y update \
        && apt-get -y upgrade \
        && apt-get -y --no-install-recommends install build-essential \
                                                      git \
                                                      curl \
                                                      wget \
                                                      sudo \
        && apt-get -y install python3 \
                              python3-pip \
        && rm -rf /var/lib/apt/lists/* \
        && update-alternatives --install /usr/bin/python python /usr/bin/python3 1 \
        && update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 1 \
        && pip install cloudmesh-installer

RUN mkdir cm
WORKDIR cm

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
