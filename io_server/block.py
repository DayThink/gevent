# -*- coding: utf-8 -*-
import socket

HOST = '127.0.0.1'                 # Symbolic name meaning the local host
PORT = 8080                        # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

print 'Server start at: %s:%s' %(HOST, PORT)
print 'wait for connection...'

while 1:
    conn, addr = s.accept()
    # print 'Connected by', addr

    data = conn.recv(1024)
    if not data:
        break
    # conn.send(data)
    print 'in server, recive data = [%s]' % data
    conn.send('Hello client, I am server'.encode('utf8'))
conn.close()