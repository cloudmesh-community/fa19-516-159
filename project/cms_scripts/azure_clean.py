from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
from cloudmesh.mongo.CmDatabase import CmDatabase
from cloudmesh.common.Shell import Shell
from cloudmesh.common.debug import VERBOSE
from cloudmesh.common.util import HEADING
import os


def azure_delete():
        print("setting cloud to azure")
        Shell.execute("cms set cloud=azure",shell=True)
        print("deleting austin-vm-azure_a1...")
        Shell.execute("cms vm delete austin-vm-azure_a1", shell=True)


if __name__== "__main__":
        azure_delete()
