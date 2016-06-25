# Writing a simple script to connect to a
# website and download a simple text file

import socket

newSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
newSock.connect(('www.py4inf.com', 80))

newSock.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')
while True:
    data = newSock.recv(512)
    if len(data) < 1:
        break
    print (data)
newSock.close()
