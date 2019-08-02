# -*- coding: utf-8 -*-
from meClass.cbt_project.cbt_demo.wn_suite.open_browser import openBrowser


class wnSell:
    def __init__(self):
        self.dr = openBrowser.open_test()

    def sell(self):
        self.dr.find_element_by_id('barcode').send_keys('12345')
        self.dr.find_element_by_xpath('/html/body/div[4]/div[1]/div/div[1]/form/button').click()




