# -*- coding: utf-8 -*-
from threading import Thread
from socket import *
import threading, time


def client(server_ip, port):
    c = socket(AF_INET, SOCK_STREAM)  # 套接字对象一定要加到函数内，即局部名称空间内，放在函数外则被所有线程共享，则大家公用一个套接字对象，那么客户端端口永远一样了

    try:
        c.connect((server_ip, port))
        c.send(('%s say hello %s' % (threading.current_thread().getName(), 'I am client')).encode('utf-8'))
        msg = c.recv(1024)
        print '%s : %s' % (threading.current_thread().getName(), msg.decode('utf-8'))
    except Exception as ex:
        print threading.current_thread().getName()

    # count = 0
    # while True:
    #     c.send(('%s say hello %s' % (threading.current_thread().getName(), count)).encode('utf-8'))
    #     msg = c.recv(1024)
    #     print(msg.decode('utf-8'))
    #     count += 1


if __name__ == '__main__':
    start = time.time()
    thread_list = list()
    for i in range(100):
        t = Thread(target=client, args=('127.0.0.1', 8080))
        thread_list.append(t)
        t.start()

    for item in thread_list:
        item.join()

    print('cost time = [{}] s'.format(time.time() - start))