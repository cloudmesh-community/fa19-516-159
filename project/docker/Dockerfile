# Download base image ubuntu 18.04
FROM ubuntu:18.04

MAINTAINER austin zebrowski

# Update ubuntu software

RUN apt-get update

# Install needed libraries

RUN apt-get install -y python3-pip libmysqlclient-dev gcc libssl-dev libkrb5-dev libsasl2-dev
RUN apt-get install vim -y
RUN pip3 install Flask==1.0.4
RUN pip3 install apache-airflow

# Map the airflow home directory

RUN export AIRFLOW_HOME=~/airflow

# Start airflow!

RUN airflow initdb
RUN mkdir ~/airflow/dags
#RUN airflow scheduler
#RUN airflow webserver -p 8080

# Expose ports

EXPOSE 8080:8080
