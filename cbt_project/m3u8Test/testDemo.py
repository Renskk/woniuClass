# -*- coding: utf-8 -*-
import os,time,random,requests,threading

class showDemo():
    def __init__(self):
        pass
    #解析m3u8地址
    def getAddr(self):
        with open('2000kbps.m3u8')as f:
           dataLine = f.readlines()
        data = []
        for i in range(len(dataLine)):
            if dataLine[i].strip().endswith('.ts'):
                data.append(dataLine[i].strip())
        return data

    def downloadFile(self):
        addr = self.getAddr()
        for i in range(10):
            res = requests.post('https://dco4urblvsasc.cloudfront.net/811/81095_ywfZjAuP/game/%s'%addr[i])
            with open('./%s'%addr[i],'wb') as f:
                f.write(res.content)



if __name__ == '__main__':
    showDemo().downloadFile()