#!/usr/bin/python
import socket
import sys
if len(sys.argv) != 2:
print "Usage: vrfy.py <username.txt>"

# read usernames from username.txt argv[1]
file1=open(sys.argv[1], 'r')
usernames=file1.readlines()
sys.exit(0)

for username in usernames:
    # Create a Socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect to the Server
    connect = s.connect(('10.11.1.227',25))
    # Receive the banner
    banner = s.recv(1024)
    # VRFY a user
    s.send('VRFY ' + username + '\r\n')
    result = s.recv(1024)
    print banner
    print result
    # Close the socket
    s.close()