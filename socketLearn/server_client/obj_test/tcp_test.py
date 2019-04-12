import socket,time

class tcp_dome():
    # def test_tcp(self):
    #     for i in range(1,4):
    #         soc = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
    #         soc.connect(('192.168.8.123',554))
    #         soc.send('这是个测试'.encode('GB2312'))
    #         soc.close()

    def udp_test(self):
        soc = socket.socket()#family=socket.AF_INET,type=socket.SOCK_DGRAM
        soc.connect(('192.168.2.104',9999))
        pacaketID =str(time.time())
        name='测试会长'
        host='测试'
        command = str(0x00000020)
        content ='入会不？'
        msg='1.0:'+pacaketID+':'+name+':'+host+':'+command+':'+content
        soc.send(msg.encode())#'GB2312'
        soc.close()


if __name__ == '__main__':
    tcp_dome().udp_test()
