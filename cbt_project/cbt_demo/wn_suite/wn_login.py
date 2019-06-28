# -*- coding: utf-8 -*-
from meClass.cbt_project.cbt_demo.wn_suite.open_browser import openBrowser


class wnLogin:
    def __init__(self):
        self.dr = openBrowser.open_test()

    def login(self):
        self.dr.find_element_by_id('username').send_keys('admin')
        self.dr.find_element_by_id('password').send_keys('')
        self.dr.find_element_by_id('verifycode').send_keys('0000')
        self.dr.find_element_by_xpath('/html/body/div[4]/div/form/div[6]/button').click()

