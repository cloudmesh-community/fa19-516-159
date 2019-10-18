from cloudmesh.common.util import banner
from cloudmesh.common.util import HEADING
from cloudmesh.common.debug import VERBOSE
from cloudmesh.common.variables import Variables
import os


def cms_boot():
    banner("cms vm boot")
    # os.system("cms vm boot")

def create_vm(name):

    variables = Variables()

    variables['debug'] = True
    variables['trace'] = True
    variables['verbose'] = 10

    banner(f"running vm: {name}")

def cms_delete():
    banner("cms vm delete")
    # os.system("cms vm delete")