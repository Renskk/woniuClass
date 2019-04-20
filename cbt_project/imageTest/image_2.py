# -*- coding: utf-8 -*-
import os,random,time,uiautomation,logging,threading
from selenium import webdriver
from pykeyboard import PyKeyboard
from pymouse import PyMouse
from PIL import ImageGrab
from woniuCBT.imageTest.image_1 import ImageMatch

logging.basicConfig(level=logging.INFO,format='%(asctime)s-%(levelname)s-%(message)s')
                    #filename='./data/'+time.strftime("%Y%m%d_%H%M%S.log"),filemode = 'w'
class pysikulix:
    def __init__(self):
        self.mouse = PyMouse()
        self.keyboard = PyKeyboard()
        self.dr = webdriver.Chrome()
        self.dr.maximize_window()
        self.dr.get('http://192.168.7.20:8080/WoniuSales/')


    # 鼠标左单击
    def click_left_mouse(self,image):
        x,y = ImageMatch().find_image(image)
        self.mouse.click(x=x, y=y, button=1, n=1)
        logging.info('click_left_mouse:%d,%d' % (x, y))

    # 鼠标右单击
    def click_right_mouse(self,image):
        x, y = ImageMatch().find_image(image)
        self.mouse.click(x=x, y=y, button=2, n=1)
        logging.info('click_right_mouse:%d,%d' % (x, y))

    # 鼠标左双击
    def click_double_left_mouse(self,image):
        x, y = ImageMatch().find_image(image)
        self.mouse.click(x=x, y=y, button=1, n=2)
        logging.info('click_double_left_mouse:%d,%d' % (x, y))

    # 鼠标中间键单击
    def click_middle_mouse(self,image):
        x, y = ImageMatch().find_image(image)
        self.mouse.click(x=x, y=y, button=3, n=1)
        logging.info('click_middle_mouse:%d,%d' % (x, y))

    #输入参数
    def input_data(self,image,string):
        x, y = ImageMatch().find_image(image)
        self.mouse.click(x=x, y=y, button=1, n=1)
        self.keyboard.type_string(string)
        logging.info('input_data:%s' % string)


if __name__ == '__main__':
    py = pysikulix()
    py.input_data('image_data/username.png','admin')
    py.input_data('image_data/password.png','admin')
    py.input_data('image_data/verifycode.png','0000')
    py.click_left_mouse('image_data/login.png')
    py.input_data('image_data/inputdata.png','12345')
    py.click_left_mouse('image_data/click01.png')
    py.click_left_mouse('image_data/click02.png')
    py.click_left_mouse('image_data/click02.png')
    py.click_left_mouse('image_data/click03.png')
    py.click_left_mouse('image_data/click04.png')


