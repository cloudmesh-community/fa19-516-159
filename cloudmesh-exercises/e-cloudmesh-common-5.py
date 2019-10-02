# Austin Zebrowski

# E.Cloudmesh.Common.5
# Develop a program that demonstrates the use of cloudmesh.common.StopWatch

from cloudmesh.common.StopWatch import StopWatch
from time import sleep

StopWatch.start("test")
sleep(2)
StopWatch.stop("test")

print("You slept for", StopWatch.get("test"), "seconds")