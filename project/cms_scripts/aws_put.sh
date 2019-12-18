#!/bin/bash
mkdir /cm/ssh
cp /root/.ssh/id_rsa /cm/ssh
chmod 400 /cm/ssh/id_rsa
touch ../testme.txt
aws_public_ip="34.223.207.106"
scp_call="sshpass -f "/root/config_s/pass.txt" scp -i '/cm/ssh/id_rsa' /cm/testme.txt ubuntu@"
target_location=":~"
put_file=$scp_call$aws_public_ip$target_location
eval $put_file
