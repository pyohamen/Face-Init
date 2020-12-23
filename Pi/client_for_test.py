import socket
import sys
import os
s = socket.socket()
num=7
s.connect(("192.168.0.29",9999))
s.send(bytes(str(num),'utf8'))
s.close()
