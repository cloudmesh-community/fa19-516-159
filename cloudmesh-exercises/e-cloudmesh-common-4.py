# Austin Zebrowski

# E.Cloudmesh.Common.4
# Develop a program that demonstrates the use of cloudmesh.common.Shell

from cloudmesh.common.Shell import Shell

mydir = Shell.pwd()
print("Your current working directory is:", mydir)