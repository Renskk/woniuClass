# -*- coding: utf-8 -*-
import os,time,requests
from woniuCBT.cbt_demo.woniu_suite.woniusales_login import woniuLogin

class CmdList:
    def __init__(self):
        pass

    def svn_demo1(self):
        os.system('chcp 65001')
        try:
            os.system(r'svn update C:\Users\Linger\Desktop\stupid_home')
        except:
            os.system(r'svn checkout http://localhost/svn/stupid_home/ C:\Users\Linger\Desktop\stupid _home --username admin --password 123456')
        os.system(r'ant -f C:\Users\Linger\Desktop\stupid_home\build.xml')
        if os.path.exists(r'E:\xampp\tomcat\webapps\woniusales'):
            os.system(r'rd /S /Q E:\xampp\tomcat\webapps\woniusales')
            os.system(r'del /S /Q E:\xampp\tomcat\webapps\woniusales.war')
        os.system(r'move C:\Users\Linger\Desktop\stupid_home\woniusales.war E:\xampp\tomcat\webapps\woniusales.war')
        try:
            requests.get('http://localhost:8081')
        except:
            os.system('startup.bat')
            time.sleep(20)
        woniuLogin().login()



if __name__ == '__main__':
    CmdList().svn_demo1()


