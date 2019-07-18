import socket
import sys
from threading import Thread
from PyQt5.QtWidgets import *

class frame(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        c = socket.socket()
        c.connect(('192.168.2.202',9999))
        self.setGeometry(450, 250, 750, 600)
        self.setWindowTitle('老年人文娱中心')
        self.add_ui()
        self.c = c
        Thread(target=self.recv_msg,daemon=True).start()

    def add_ui(self):
        line = QLineEdit(self)
        line.setGeometry(0,500,650,100)
        self.line = line
        btn =QPushButton('发送',self)
        btn.setGeometry(650,500,100,100)
        btn.clicked.connect(self.send_msg)
        tb = QTextBrowser(self)
        tb.setGeometry(0,0,750,500)
        self.tb = tb

    def send_msg(self):
        content = self.line.text()
        if content != '':
            self.c.send(content.encode())
            self.line.clear()

    def recv_msg(self):
        while 1 :
            chat_content = self.c.recv(1024).decode()
            self.tb.append(chat_content)

if __name__ == '__main__':
    app = QApplication([])
    f = frame()
    f.show()
    sys.exit(app.exec())

