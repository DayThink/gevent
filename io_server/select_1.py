# -*- coding: utf-8 -*-
import socket
import select

HOST = '127.0.0.1'
PORT = 8080

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((HOST, PORT))
socket.listen(5)
inputs = [socket]

print 'Server start at: %s:%s' %(HOST, PORT)
print 'wait for connection...'

while True:
    infds, outfds, errfds = select.select(inputs, inputs, [], 5)
    if len(infds) != 0:
        # print 'enter infds'
        for fds in infds:
            try:
                if fds is socket:
                    clientsock, clientaddr = fds.accept()
                    inputs.append(clientsock)
                    # print 'connect from:', clientaddr
                else:
                    # print 'enter data recv'
                    data = fds.recv(1024)

                    if not data:
                        inputs.remove(fds)
                    else:
                        print data
            except Exception as ex:
                pass

    if len(outfds) != 0:
        # print 'enter outfds'
        for fds in outfds:
            try:
                fds.send("python select server from Debian.\n")
            except Exception as ex:
                pass