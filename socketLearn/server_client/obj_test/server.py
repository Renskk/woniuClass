import  socket

class ser:
    def __init__(self):
        self.s=socket.socket()
        self.s.bind(('192.168.2.110',9999))
        self.s.listen(5)

    #接受客户端连接
    def get_c(self):
        s = self.s
        li = []
        #接受客户端连接
        con,addr = s.accept()
