# -*- coding: utf-8 -*-
from selenium import webdriver
import time

class GuiDemo:
    def __init__(self):
        self.dr = webdriver.Chrome()
        self.dr.get('http://localhost:8080/WoniuBoss2.0/')
        self.dr.maximize_window()

    def test01(self,username,password,checkcode):
        self.dr.find_element_by_name('userName').send_keys(username)
        self.dr.find_element_by_name('userPass').send_keys(password)
        self.dr.find_element_by_name('checkcode').clear()
        self.dr.find_element_by_name('checkcode').send_keys(checkcode)
        self.dr.find_element_by_xpath('//*[@id="form-login"]/div/div/div[2]/button').click()
        if self.dr.find_element_by_link_text('注销'):
            return True
        else:
            return False

