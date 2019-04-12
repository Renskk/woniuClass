import socket
from threading import Thread
#建立和服务器连接
class cli ():
    def __init__(self):
        self.c = socket.socket()
        self.c.connect(('192.168.2.202',9999))
        Thread(target=self.b).start()
        self.a()

    def a(self):
        while 1:
            a = input('')
            self.c.send(a.encode())

    def b(self):
        while 1:
            date = self.c.recv(1024)
            print(date.decode())

cli()

