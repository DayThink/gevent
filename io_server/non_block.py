# -*- coding: utf-8 -*-
from io import BlockingIOError
from socket import *

HOST = '127.0.0.1'                 # Symbolic name meaning the local host
PORT = 8080

server = socket(AF_INET, SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)
server.setblocking(False)

print 'Server start at: %s:%s' %(HOST, PORT)
print 'wait for connection...'

conn_l=[]

while True:
    try:
        conn, addr = server.accept()
        conn_l.append(conn)
        print(addr)
    except BlockingIOError:
        print('do other work',len(conn_l))
        del_l = []
        for conn in conn_l:
            try:
                data=conn.recv(1024)
                if not data:
                    conn.close()
                    del_l.append(conn)
                    continue
                conn.send(data.upper())
            except BlockingIOError:
                pass
            except Exception:
                conn.close()
                del_l.append(conn)

        for conn in del_l:
            conn_l.remove(conn)