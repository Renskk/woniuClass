# -*- coding: utf-8 -*-
from meClass.cbt_project.cbt_demo.wn_suite.open_browser import openBrowser


class sellPart:
    def __init__(self):
        self.dr = openBrowser.open_test()

    def barcode(self):
        self.dr.find_element_by_id('barcode').clear()
        return  self.dr.find_element_by_id('barcode')

    def ensure_button(self):
        return self.dr.find_element_by_xpath("/html/body/div[4]/div[1]/div/div[1]/form/button")
