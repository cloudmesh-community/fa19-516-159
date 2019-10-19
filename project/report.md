# Creating a Data Pipeline between HDFS and AWS Redshift

Austin Zebrowski, fa19-516-159 :o2:

## Abstract

I will use Apache Airflow to create a data pipeline from Azure Blob containers to AWS S3. I will create a REST API that allows the user to use GET to get a list of the files on either of the clouds, and to use POST to move a file between clouds. 

I will create a cloudmesh.airflow library that allows us to easily use Cloudmesh in the context of an Airflow DAG.

## Introduction

Cloudmesh is a great tool for using the resources of multiple clouds. One of Cloudmesh's features is cloudmesh-storage, which enables cloud-to-cloud data transfer. This meets a key need, but often want to do more than simply move the files. This is where Aiflow comes into play.

With Airflow, we are able to set up directed acyclic graphs (DAGs) that define a sequence of tasks in a workflow. We can then view these DAGs in a UI that displays their definitions, histories, and execution logs. What kind of tasks can we perform in Airflow? Practically anything! Airflow is a open-source, python based cloud technology. We can leverage the full power of Python to perform any tasks required for our DAG.

We can combine the capabilities of Cloudmesh and Airflow to get the best of both worlds. Within an Airflow DAG, we can use Cloudmesh to start VMs on multiple clouds and move data between those clouds. 

## Design

TBD


## Implementation

* Technologies Used

    1) Apache Airflow (open source, python-based data pipeline)
    2) Azure Blob
    3) AWS S3
    4) Cloudmesh
    5) Connexion

## Progress

10/18

Installed a fully operable instance of Cloudmesh. Previous Cloudmesh installation was not fully functional due to a problem in my environment. 

Installed Airflow.

## Work Breakdown

All of this work is to be completed by Austin Zebrowski. This is not a group project.

## References

## Results

TBD

* Deployment Benchmarks
* Application Benchmarks
