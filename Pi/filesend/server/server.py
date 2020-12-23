import socket
import sys
import zipfile
import os

port = 9999

ss = socket.socket()
print('[+] Server socket is created.')

ss.bind(('', port))
print('[+] Socket is binded to {}'.format(port))

ss.listen(5)
print('[+] Waiting for connection...')

con, addr = ss.accept()
print('[+] Got connection from {}'.format(addr[0]))
l = con.recv(1024)
if(l):
    filename="dataset.zip"
    f = open(filename, 'wb')
    while(l):
        f.write(l)
        l = con.recv(1024)
    f.close()
    print('[+] Received file ' + filename)
    with zipfile.ZipFile(filename, 'r') as file:
        print('[+] Extracting files...')
        file.extractall('./dataset')
        print('[+] Done')
    os.remove(filename)
else:
    print("'dataset.zip' doesn't exist on client")
con.close()
ss.close()