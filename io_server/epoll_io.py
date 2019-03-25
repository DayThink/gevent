# -*- coding: utf-8 -*-
import socket
import select
import selectors2 as selectors
# uage: https://github.com/sethmlarson/selectors2
s = selectors.DefaultSelector()


HOST = '127.0.0.1'
PORT = 8080

s = socket.socket()
s.bind((HOST, PORT))
s.listen(5)
epoll_obj = select.epoll()
epoll_obj.register(s, select.EPOLLIN)
connections = {}


print 'Server start at: %s:%s' %(HOST, PORT)
print 'wait for connection...'

while True:
    events = epoll_obj.poll()
    for fd, event in events:
        print(fd, event)
        if fd == s.fileno():
            conn, addr = s.accept()
            connections[conn.fileno()] = conn
            epoll_obj.register(conn, select.EPOLLIN)
            msg = conn.recv(200)
            conn.sendall('ok'.encode())
        else:
            try:
                fd_obj = connections[fd]
                msg = fd_obj.recv(200)
                fd_obj.sendall('ok'.encode())
            except Exception:
                epoll_obj.unregister(fd)
                connections[fd].close()
                del connections[fd]

s.close()
epoll_obj.close()