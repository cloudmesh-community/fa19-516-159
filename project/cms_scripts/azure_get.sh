#!/bin/bash


aws_public_ip="34.223.207.106"
azure_public_ip="10.0.0.9"
scp_get="scp -i '/cm/ssh/id_rsa' ubuntu@"
target_location="/cm"
source_location=":/home/ubuntu/testme.txt "
get_file=$scp_get$aws_public_ip$source_location$target_location

eval $get_file

scp_put="scp -i '/cm/ssh/id_rsa' TBD@"
source_location=":~/testme.txt"
target_location=" /cm"
put_file="$scp_put$azure_public_ip$source_location$target_location"

eval $put_file
