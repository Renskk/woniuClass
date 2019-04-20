# -*- coding: utf-8 -*-
from woniuCBT.cbt_demo.woniu_suite.open_browser import openBrowser


class woniuLogin:
    def __init__(self):
        self.dr = openBrowser.open_test()

    def login(self):
        self.dr.find_element_by_id('username').send_keys('admin')
        self.dr.find_element_by_id('password').send_keys('')
        self.dr.find_element_by_id('verifycode').send_keys('0000')
        self.dr.find_element_by_xpath('/html/body/div[4]/div/form/div[6]/button').click()

