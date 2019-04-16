from pykeyboard import PyKeyboard
from pymouse import PyMouse
import time, random, os, threading

# time.sleep(3)
# mouse = PyMouse()
# # mouse.move(1200, 200)
#
# for i in range(5):
#     x = random.randint(300, 1300)
#     y = random.randint(200, 800)
#     mouse.move(x, y)
#     time.sleep(1)
#
# mouse.click()
#
# keyboard = PyKeyboard()
# keyboard.type_string()

# os.system("adb shell input text Hello")


# def test_run():
#     for i in range(10):
#         print("线程 %s 正在运行." % threading.current_thread().getName())
#         time.sleep(1)
#
# if __name__ == '__main__':
#     print("主线程正在运行.")
#     t = threading.Thread(target=test_run)
#     t.setDaemon(True)
#     t.start()
#     # t.join()
#
#     for i in range(5):
#         print("主线程正在运行.")
#         time.sleep(1)
#
#     print("主线程结束运行.")


# import random
#
# content = ["Woniuxy", "123456", "Good Night", "Tomorrow Better!",
#                    "Testing", "666667788", "123.45", "2018-08-06", "12", "8", "你好"]
# print(random.sample(content, 1)[0])
# print(random.choice(content))


# import os
#
# result = os.popen("tasklist | findstr firefox.exe").read()
#
# print(result)
#
# if "firefox.exe" in result:
#     print("进程还活着")
# else:
#     print("Death")




# import uiautomation, os, time
#
# # os.popen(r'"C:\Program Files (x86)\Mozilla Firefox 61\firefox.exe" http://localhost:8088/woniusales')
# # time.sleep(5)
# firefox_window = uiautomation.WindowControl(ClassName="MozillaWindowClass")
# print(firefox_window.Name)
# print(firefox_window.BoundingRectangle)
# time.sleep(2)
# firefox_window.Maximize()
# firefox_window.SetTopmost()
# uiautomation.Win32API.SetForegroundWindow(firefox_window.Handle)
#


# from PIL import ImageGrab
#
# time.sleep(3)
# now_time = time.strftime("%Y%m%d_%H%M%S.png")
# ImageGrab.grab().save('./screenshot/' + now_time)


# from PIL import Image, ImageGrab
#
# screen = ImageGrab.grab().convert('RGBA')
# small = Image.open('./screenshot/woniusales_username.png')
#
# print(screen.size)
# print(small.size)
#
# print(screen.load()[5, 20])
# print(small.load()[30, 40])
#
# test = Image.open(r'C:\Users\Denny\Pictures\启动画面 2.jpg')
# print(test.load()[50, 30])


# import socket
#
# s = socket.socket()
#
# ip = 5000
#
# while True:
#     try:
#         s.connect(('127.0.0.1', ip))
#         print("%d 已经被占用" % ip)
#         ip += 1
#     except:
#         print("%d 没有被占用" % ip)
#         break
#


# template = '<title>${title}</title>'
# title = 'HTML报告'
# template = template.replace('${title}', title)
# print(template)


import os, shutil

# svn diff -r {2019-04-08} --summarize https://localhost:8443/svn/WoniuSales
# svn checkout https://localhost:8443/svn/WoniuSales F:/WoniuSales --username denny --password 123456
# 最后一行表示本次checkout的最后版本，保存该版本号后即可获取更新的修改
# changed = os.popen('svn diff -r 3:HEAD --summarize https://localhost:8443/svn/WoniuSales').read()
# print(changed)
# os.system()
# shutil.copy('F:/WoniuSales/woniusales.war', 'C:/Tools/Tomcat8.0/webapps/woniusales.war')
# time.sleep(3)
# os.system(r'C:\Tools\Tomcat8.0\bin\shutdown.bat')


# str = 'Open Browser'
# str = str.replace(' ', '_').lower()
# print(str)

# str = "xpath=(//button[@type='button'])"
# print(str.split('=', 1))


# def prime(min, max):
#     for number in range(min, max):
#         count = 0
#         for i in range(1, number+1):
#             if number % i == 0:
#                 count += 1
#         if count == 2:
#             print(f"{number} 是一个质数.")
#
# def test():
#     min = int(input("请输入最小范围："))
#     max = int(input("请输入最大范围："))
#     prime(min, max)
#
# test()


# os.chdir('D:/')
# print(os.popen('dir').read())


print(os.path.exists('F:/WoniuSalesX'))