#!/bin/python


file1=open ('access_log.txt','r')
lines =file1.readlines()
#print (type(lines)) --list
jsfiles=[]
for line in lines:
    if ".js" in line:
        line=line.split("HTTP/1.1")[0]
        line=line.split("/")[4]
        jsfiles.append(line)
jsfiles=list(set(jsfiles))
print(jsfiles)
         