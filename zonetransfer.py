#!/bin/python
import os
import sys

domain=sys.argv[1]
filename=domain +".txt"
cmd="host -t ns "+domain +">"+filename
os.system(cmd)

file1=open (filename, 'r' )
servers= file1.readlines()
for server in servers:
    server= server.split("server")[1]
    cmd ="host -l "+domain +server
    os.system(cmd) 
