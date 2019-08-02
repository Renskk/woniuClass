# -*- coding: utf-8 -*-
import time
from selenium import webdriver
class openBrowser:
    driver = None

    def __init__(self):
        pass

    @classmethod
    def open_test(cls):
        if openBrowser.driver is None:
            openBrowser.driver = webdriver.Chrome()
            openBrowser.driver.maximize_window()
            openBrowser.driver.get('http://localhost:8081/wn/')
            time.sleep(0.5)
        return openBrowser.driver
