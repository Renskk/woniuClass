# -*- coding: utf-8 -*-
import os,time,random,uiautomation
import uiautomation as auto
from pykeyboard import PyKeyboard
from pymouse import PyMouse
os.popen('Calc.exe')
# mouse = PyMouse()
# time.sleep(1)
# mouse.click(1182,100,button=1,n=1)
# for i in range(200):
#     x = random.randint(0,1536)
#     y = random.randint(45,800)
#     bu = random.randint(1,3)
#     n = random.randint(1,2)
#     print('x,y',x,y)
#     mouse.click(x,y,button=bu,n=n)
calcWindow = auto.WalkControl()
