# Austin Zebrowski

# E.Cloudmesh.Common.1
# Develop a program that demonstrates the use of banner, HEADING, and VERBOSE

from cloudmesh.common.util import banner
from cloudmesh.common.util import HEADING
from cloudmesh.common.debug import VERBOSE
from cloudmesh.common.variables import Variables

variables = Variables()

variables['debug'] = True
variables['trace'] = True
variables['verbose'] = 10

def setbanner():
    HEADING()
    banner("this is my banner!")


def debugme():
    verboseexample = {"verbose key": "verbose value"}
    VERBOSE(verboseexample)

setbanner()
debugme()