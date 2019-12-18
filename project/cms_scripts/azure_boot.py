from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
from cloudmesh.mongo.CmDatabase import CmDatabase
from cloudmesh.common.Shell import Shell
from cloudmesh.common.debug import VERBOSE
from cloudmesh.common.util import HEADING
import os

def azure_boot():
        print("booting austin-vm-azure_a1...")
        Shell.execute("cms vm boot --name=austin-vm-azure_a1 --key=austin", shell=True)


def create_azure_vm():
        print("intializing...")
        Shell.execute("cms init", shell=True)
        print("setting cloud...")
        Shell.execute("cms set cloud=azure", shell=True)
        print("adding key...")
        Shell.execute("cms key add austin --source=ssh", shell=True)
        print("getting database information...")
        cm = CmDatabase()
        if cm.collection('austin-vm-azure_a1').estimated_document_count() > 0:
            print("specified vm already exists... deleting old vm...")
            azure_delete()
            azure_boot()
        else:
            print("specified vm does not exist... booting vm...")
            azure_boot()


def azure_delete():
        print("deleting old vm...")
        Shell.execute("cms vm delete austin-vm-azure_a1", shell=True)


if __name__== "__main__":
        create_azure_vm()
