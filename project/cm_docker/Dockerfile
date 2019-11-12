# Download base image ubuntu 19.04
FROM ubuntu:19.04

MAINTAINER austin zebrowski

# Update ubuntu software

RUN apt-get update

# Install needed libraries

RUN apt-get install -y openssl curl
RUN apt-get install vim -y python3-pip
RUN apt-get install -y python-setuptools python-dev build-essential

RUN pip3 install --upgrade pip
RUN pip3 install cloudmesh-installer

