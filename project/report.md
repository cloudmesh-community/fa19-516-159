# AWS to Azure Data Pipeline: Using Cloudmesh in Airflow

Austin Zebrowski, fa19-516-159 :o2:

azebrows@iu.edu

## Abstract

Cloudmesh enables easy creation of virtual machines (VMs) in multiple clouds. Apache Airflow is an open-source data pipeline orchestration tool. By leveraging the strengths of each, files can be moved between clouds, and the files' status and history can be viewed through a user interface (UI). This can be achieved by creating a library of functions that uses Cloudmesh commands in an Airflow environment.

## Introduction

Cloudmesh is a great tool for using the resources of multiple clouds. One of Cloudmesh's features is cloudmesh-storage, which enables cloud-to-cloud data transfer. This meets a key need, but often want to do more than simply move the files. This is where we can use Airflow - a python-based open source data pipelining project.

With Airflow, we can configure directed acyclic graphs (DAGs) that define a sequence of tasks in a workflow. We can then view these DAGs in a UI that displays their schedules, code definitions, histories, and execution logs. By creating a library of functions that uses Cloudmesh within Airflow, we can easily schedule and visualize the startup of VMs on multiple clouds and a data transfer between these clouds.

To make these capabilities broadly accessible, we create a RESTful API that exposes functionality such as starting VMs, listing files, and moving files.

## Architecture

![Architecture](/project/images/architecture_image.PNG)

## Implementation

* Technologies Used

    1) Apache Airflow
    2) Azure Blob
    3) AWS S3
    4) Cloudmesh
    5) Docker
    6) Open API 3.0

## Progress

10/18

Installed a fully operable instance of Cloudmesh. Previous Cloudmesh installation was not fully functional due to a problem in my environment. 

10/20

Created Amazon AWS account. added "cloudmesh" user, and added access key information into cloudmesh.yaml. Attempted, unsuccessfully, to launch an AWS VM with Cloudmesh (can not refresh image list).

10/21

Created [dockerfile](/project/docker/Dockerfile) and [docker compose file](/project/docker/docker-compose.yaml) to spin up a Docker container running Airflow.

10/24

Created architecture diagram.


## Work Breakdown

All of this work is to be completed by Austin Zebrowski. This is not a group project.

## References

## Results

TBD

* Deployment Benchmarks
* Application Benchmarks
