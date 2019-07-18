import os
import socket
from threading import Thread

class a():
    def __init__(self):
        # 服务器的套接字对象
        self.s = socket.socket()
        # 绑定IP和端口
        self.s.bind(('192.168.2.202', 9999))
        # 监听
        self.s.listen(5)

    # 接受客户端连接
    def get_con(self):
        s = self.s
        li = []
        while 1:
            # 接受客户端连接
            con, addr = s.accept()
            # print('客户端消息：',con.recv(1024).decode())
            # con.send('aaa'.encode())
            li.append(con)
            con.send('请输入用户名：'.encode())
            try:
                name = con.recv(1024)
            except:
                continue
            names = name.decode()
            Thread(target=self.b, args=(con, addr, li, name, names)).start()

    def b(self, con, addr, li, name, names):
        while 1:
            try:
                data = con.recv(1024)
            except:
                print('%s退出' % names)
                # data = ''
                #     if con in li:
                li.remove(con)
                break
            if data != '':
                print(data.decode())
            # data = con.recv(1024)
            # print(data.decode())
            # con.send(data)
            for i in li:
                if data != '':
                    i.send(name + '说：'.encode() + data)

a().get_con()
