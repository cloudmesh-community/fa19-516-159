@echo off
SETLOCAL
SET nametag=cms

type ..\..\VERSION > tempVersion
SET /p VERSION= < tempVersion
del tempVersion

SET tag=latest

CALL :banner "Building cloudmesh/cloudmesh-%nametag%"
CALL :image %nametag% %VERSION% %tag%
CALL :banner "Tagged cloudmesh/cloudmesh-%nametag%:%VERSION% cloudmesh/cloudmesh-%nametag%:%tag%"
EXIT /B %ERRORLEVEL%

:banner
ECHO ###################################
ECHO %~1
ECHO ###################################
EXIT /B 0

:image
docker build --no-cache -t cloudmesh/cloudmesh-%~1:%~2 .
docker tag cloudmesh/cloudmesh-%~1:%~2 cloudmesh/cloudmesh-%~1:%~3
EXIT /B 0

