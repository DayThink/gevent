# -*- coding: utf-8 -*-
from gevent import monkey;
monkey.patch_all()

from socket import *
import gevent

HOST = '127.0.0.1'
PORT = 8080

# 如果不想用monkey.patch_all()打补丁，可以用gevent自带的socket
# from gevent import socket
# s = socket.socket()

def server(server_ip, port):
    print 'Server start at: %s:%s' % (HOST, PORT)
    print 'wait for connection...'

    s = socket(AF_INET, SOCK_STREAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind((server_ip, port))
    s.listen(5)

    while True:
        conn, addr = s.accept()
        gevent.spawn(do_woke, conn, addr)


def do_woke(conn, addr):
    try:
        # while True:
            res = conn.recv(1024)
            print('client %s:%s msg: %s' % (addr[0], addr[1], res))
            conn.send(res.upper())
    except Exception as e:
        print(e)

    finally:
        conn.close()


if __name__ == '__main__':
    server('127.0.0.1', 8080)