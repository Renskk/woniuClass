# -*- coding: utf-8 -*-
import logging, time
from selenium import webdriver
from pykeyboard import PyKeyboard
from pymouse import PyMouse
from opencv_learn.get_coord import ctr

logging.basicConfig(level=logging.INFO, format='%(asctime)s-%(levelname)s-%(message)s')


# filename='./data/'+time.strftime("%Y%m%d_%H%M%S.log"),filemode = 'w'

class pysikulix:
    def __init__(self):
        self.mouse = PyMouse()
        self.keyboard = PyKeyboard()
        self.dr = webdriver.Chrome()
        self.dr.maximize_window()
        self.dr.get('http://39.106.93.201/signIn')


    # 鼠标左单击
    def click_left_mouse(self, image_temp):
        x, y = ctr().opencv2(image_temp)
        self.mouse.click(x=int(x), y=int(y), button=1, n=1)
        logging.info('click_left_mouse:%d,%d' % (x, y))

    # 鼠标右单击
    def click_right_mouse(self, image_temp):
        x, y = ctr().opencv2(image_temp)
        self.mouse.click(x=int(x), y=int(y), button=2, n=1)
        logging.info('click_right_mouse:%d,%d' % (x, y))

    # 鼠标左双击
    def click_double_left_mouse(self, image_temp):
        x, y = ctr().opencv2(image_temp)
        self.mouse.click(x=int(x), y=int(y), button=1, n=2)
        logging.info('click_double_left_mouse:%d,%d' % (x, y))

    # 鼠标中间键单击
    def click_middle_mouse(self, image_temp):
        x, y = ctr().opencv2(image_temp)
        self.mouse.click(x=int(x), y=int(y), button=3, n=1)
        logging.info('click_middle_mouse:%d,%d' % (x, y))

    # 输入参数
    def input_data(self, image_temp, string):
        while 1:
            try:
                x, y = ctr().opencv2(image_temp)
                self.mouse.click(x=int(x), y=int(y), button=1, n=1)
                self.keyboard.type_string(string)
                logging.info('input_data:%s' % string)
                break
            except :
                continue


if __name__ == '__main__':
    py = pysikulix()
    py.input_data('image/username.png', '18581619336')
    py.input_data('image/passwd.png', '123456')
    py.click_left_mouse('image/login.png')
