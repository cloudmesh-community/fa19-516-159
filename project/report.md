# Using Cloudmesh in Airflow - Azure and AWS

Austin Zebrowski, fa19-516-159

azebrows@iu.edu

## Abstract

Cloudmesh enables easy creation of virtual machines (VMs) in multiple
clouds. Apache Airflow is an open-source data pipeline orchestration
tool. By leveraging the strengths of each, files can be moved between
clouds, and the files' status and history can be viewed through a user
interface (UI). This can be achieved by creating a library of functions
that uses Cloudmesh commands in an Airflow environment.

## Introduction

With Airflow, we can configure directed acyclic graphs (DAGs) that
define a sequence of tasks in a workflow. We can then view these DAGs in
a UI that displays their schedules, code definitions, histories, and
execution logs. By creating a library of functions that uses Cloudmesh
within Airflow, we can easily schedule and visualize the startup of VMs
on multiple clouds and subsequent interactions with these clouds.

## Cloudmesh Airflow Architecture

:o2: image missing

![Architecture](/project/images/architecture_image.PNG)


### Motivation 

Cloudmesh enables users to easily work in a variety of cloud environments. With this, there can be some difficulty to keep environments neatly managed.
For instance, a user can spin up 3 VMs in different environments and easily forget to clean up when they are finished using them. It is also likely that a user
may skip a step when beginning to work on a new cloud. It is possible, too, that a user will repeat steps that they have already completed, simply because 
they cannot remember what has or has not been done. Managing Cloudmesh's workflow and work environment can be handled in a few ways. Airflow can solve these 
problems uniquely well, though, as workflow management is its entire function. By managing Cloudmesh workflows in Airflow, a user can easily see what has 
been completed, and when. The user can also view execution and error logs, visualize dependencies between tasks, and schedule tasks - for instance, stopping
all VMs at the end of each day and starting them back up the next morning. 

### Docker Implementation

As open source projects, both Apache Airflow and Cloudmesh are constantly under development. As a result, managing versions of these project can be difficult 
to manage. As each of the projects gets updated, a user must make the same updates on their side. Moreover, these projects can have nuances when being used 
on different operating systems. For instance, Airflow is not compatible with Windows. Building these softwares in Docker helps to solve some of these problems. 
A user can easily add new functionality to their Docker images, and will be able to build on different operating systems as they please. 

## Airflow - Overview

Airflow is an task scheduler that can be used to create, visualize, and monitor workflows. Although it originated at AirBnb, Airflow 
is currently maintained by the Apache Software Foundation as an open-source project. Airflow has a lot of "out of the box" functionality but, 
because it executes native python code, the functionality of workflows is limited only by what is achievable in Python. The workflows are 
designed as Directed Acyclic Graphs (DAGs), which can be easily viewed in a Web UI. In a DAG, tasks are chained together to show dependencies. 
A task can only be reached by completing its preceding tasks, and it is not possible to complete tasks out of order.
Airflow can be configured to be run on premises, or on any cloud (AWS, GCP, Azure, etc.). 

## Airflow - Architecture

At a high level, Airflow is comprised of six architectural components: 

1. Scheduler/Executor
 The Airflow scheduler is a service that continously monitors tasks and DAGs, looking for tasks that are ready to be run. 
Task will be run at scheduled intervals, as long as all of their dependencies have been met.
2. Worker Nodes
Worker nodes are the components that execute the tasks specified in a DAG. There are three main execution types available in Airflow, and each 
execution type uses worker nodes differently. 
* In "Sequential Executor" mode, a single worker node executes tasks in sequence.
* In "Local Executor" mode, a single worker node (on the same machine as the Scheduler) executes tasks in parallel. 
* In "Celery Executor" mode, a pool of worker nodes (on a different server from the Scheduler) executes the tasks in a distributed fashion. 
3. Metadata Database
The Airflow Metadata Database contains data about task schedules, dependencies, and executions. The Airflow Scheduler reads the Metadata database to determine
which tasks are ready to be run at any given time.
4. Web UI
In the Airflow Web UI, users can view their DAGs, trigger DAG executions, configure source or destination connections, set variables, and manage user permissions. 
5. Webserver
Airflow's Web UI is enabled by a webserver, which handles the network requests and web documents relevant to the UI.
6. Log Files
Airflow's log files contain time-ordered messages about the events that occur in the Airflow environment.  
This includes actions that happen in the Web UI, task executions, and processes that happen in the background. 
The logs are stored as a Python dictionary.

The nuances of Airflow's architecture and capabilities are not discussed here. 

![Airflow_Architecture](/project/images/airflow_architecture.png)

## Results

It is achievable to run Cloudmesh and Airflow within a Docker image. Users of this image can effectively author DAGs that instruct Cloudmesh to 
initialize the MongoDB database, choose a cloud, provide keys to that cloud, and start a new VM. This functionality is proven for AWS EC2 instances 
and Azure VMs. Users are also able to schedule DAGs that clean up their environment, by deleting VMs. One can follow these patterns to orchestrate any 
sort of workflow, provided that it is possible to execute the workflow in Python, or any of the operators available in Airflow. 

A shortcoming of this work is that it takes users off the command line. Users will author dags on the command line, but when using the Airflow GUI they will 
be limited to what is possible in they GUI. This can cause some problems. For instance, certain users cannot use Azure's command line interface unless they 
manually type in their password. Since Airflow does not have a portal for authentication, this would require a complex workaround. So, it becomes a troublesome
process to use Azure's CLI within Airflow DAGs. In these cases, Cloudmesh can be a tremendous asset - it is able to simplify many cloud tasks. 

## Opportunities for Improvement

* Building Cloudmesh on Docker, and interfacing with AWS, Azure, and Chameleon reveals a few areas for improvement. Most significantly, it is possible to 
create multiple VMs with the same name. This happens when a user creates multiple VMs from the same container. It is not possible to delete these VMs in 
Cloudmesh, since they have the same name. It is possible, in AWS and Azure, to delete these VMs from the cloud's GUI. In Chameleon cloud this cause problems,
where the existing VMs cannot be deleted, and new VMs cannot be created. 

* In the cloudmesh.yaml file, the MongoDB download locations must be changed to specify a location that is not mounted as a volume to a Docker container. 

* The Cloudmesh function "vm ip show" is not working in Azure or AWS. However, it does not provide a "Not implemented" response. 

* Stopping and removing docker containers that are running cloudmesh results in a situation where Cloudmesh is not aware of any local VMs. This causes errors when trying to list VMs, for example. 

## Implementation Manual

These implementation steps assume that you have Docker and Docker Compose installed, ssh keys, and that you have cloned this repository

* Technologies Used

    1) Apache Airflow
    2) Azure VM
    3) AWS EC2
    4) Cloudmesh
    5) Docker

#### Configure Amazon AWS:
1. [Login to AWS Account](https://aws.amazon.com)
2. [Go to Identity and Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html)
	- Create 'cloudmesh' group
	- Create 'cloudmesh' user
	- Create New Access Key for user 'cloudmesh'
	- Place the Access Key ID and Secret Access Key ID in cloudmesh.yaml file
	- Place the .pem file in the ~/.cloudmesh directory
	- Specify the .pem file name in the cloudmesh.yaml file
3. [Configure the EC2 Security Groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html#creating-security-group)
	- Add an inbound custom TCP Rule with open port 22. Open this port to your PC, for SSH

	
#### Configure Azure:
1. [Login to Azure Account](https://portal.azure.com)
2. Copy your Subscription ID to a notepad
3. Go to the Registrations page, and register a 'cloudmesh' application
	- Copy your application's client and tenant IDs to a notepad
4. Go to the Certificates and Secrets page, and create a new Client Secret
	- Copy the Client Secret to a notepad
5. Go to Access Control and add cloudmesh as a contributor
6. Add the credentials from your notepad into the cloudmesh.yaml file
	

#### Local Directory Config:

This filed must NOT be copied into your image

1. Create a configuration file for your AWS Secrets, to enable SSH
	- mkdir aws
	- touch credentials
 (contents)
	[cloudmesh]
	aws_access_key_id=*****
	aws_secret_access_key=*******
2. Create a configuration file for your passcodes
	- touch pass.txt
	- specify password for scp
 
#### Modify DAGs:

1. Modify the files in the DAGs directory to use your ssh key
	

#### Cloudmesh.yaml Config:

1. Ensure that you have configured your AWS and Azure accounts (refer to those sections)
2. Fill out the MongoDB data section, specifying your mongo username and password
3. Replace the mongo path and mongo log paths, in favor of a directory that is not specified as a volume in docker-compose.yml file

	
#### Startup:

1. Build the docker image
 - docker build -t cloudmesh/cloudmesh-cms .
2. Modify volume paths in docker-compose.yml to point to your local directory
3. Run your images 
 - docker compose up -d
4. When finished, stop and remove containers
 - docker-compose down
 
#### Airflow UI

While containers are running...
1. Access the Airflow UI
 - localhost:8080
2. Turn the DAG schedulers to "on"
3. Trigger the DAGs
		
#### Run Pytests:

* pytest -q test_airflow.py
* pytest -q test_airflow.py

## References

[AWS Quickstart](https://cloudmesh.github.io/client/aws.html?highlight=aws)
[Airflow Validation Tests](https://blog.usejournal.com/testing-in-airflow-part-1-dag-validation-tests-dag-definition-tests-and-unit-tests-2aa94970570c)
[Azure Quickstart](https://github.com/cloudmesh/cloudmesh-manual/blob/master/docs-source/source/accounts/azure.md)
[Airflow Overview](https://airflow.apache.org/)
[Workflow Management](https://otonomo.io/luigi-airflow-pinball-and-chronos-comparing-workflow-management-systems/)
[Airflow Internals](https://www.astronomer.io/)
[Airflow Architecture](https://medium.com/@dustinstansbury/understanding-apache-airflows-key-concepts-a96efed52b1a)



