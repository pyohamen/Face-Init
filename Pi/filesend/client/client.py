import socket
import sys
import os
s = socket.socket()
s.connect(("localhost",9999))
if(os.path.exists("dataset.zip")):
    f = open ("dataset.zip", "rb")
    l = f.read(1024)
    while (l):
        s.send(l)
        l = f.read(1024)
else:
    print("zip file doesn't exist")
s.close()
