# -*- coding: utf-8 -
import bs4
import logging
import os
import requests
import time

logging.disable(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s-%(levelname)s-%(message)s')


class produte():
    def __init__(self):
        self.se = requests.session()

    # 获取验证码
    def htmlPic(self):
        res = self.se.get('http://www.waverlyc.com:8088/alliance/mgr/loginPage',timeout=60*4).text
        # print(res)
        soup = bs4.BeautifulSoup(res, features="html.parser")
        link = soup.select('span img ')
        jpg = link[0].get('src')
        picture = 'http://www.waverlyc.com:8088/alliance/' + jpg
        re = requests.get(picture)
        with open('C:/Users/Linger/Desktop/' + '1' + '.jpg', 'wb')as f:
            for chunk in re.iter_content(128):
                f.write(chunk)

    # 验证码取字
    def word(self):
        picturePath = r'C:\Users\Linger\Desktop\1.jpg'
        outFilePath = r'C:\Users\Linger\Desktop\1'
        programPath = r'E:\apps\Tesseract-OCR\tesseract.exe'
        cmdContext = programPath + ' ' + picturePath + ' ' + outFilePath
        os.popen(cmdContext)
        time.sleep(0.3)
        try:
            with open(r'C:\Users\Linger\Desktop\1.txt', 'r')as fb:
                # print(fb.read())
                return fb.read()
        except:
            print('读不出来！！')

    def start(self):
        print('验证码：%s' % self.word())
        logging.debug('验证码：%s' % self.word())
        try:
            res = self.se.post('http://www.waverlyc.com:8088/alliance/mgr/login',
                                {'username': 'tecstormAdmin', 'password': '12345', 'code': self.word().strip()})
            if '程序出错,请联系管理员!' in res.text:
                print('OCR背锅')
            else:
                print('得过且过')
        except:
            print('OCR背锅')


if __name__ == '__main__':
    for i in range(100):
        produte().htmlPic()
        produte().start()
