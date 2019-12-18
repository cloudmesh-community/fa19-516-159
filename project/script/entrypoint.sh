#!/usr/bin/env bash

echo "initializing db"
airflow initdb
echo "starting scheduler"
airflow scheduler &
echo "starting webserver"
exec airflow webserver
