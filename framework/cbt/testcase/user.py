import os, time, random, requests
from selenium import webdriver
from test_framework_43.woniucbt.common.tool import CommonTool as tool

class WoniuSalesUser:
    # def __init__(self):
    #     self.driver = webdriver.Firefox()
    #     self.driver.get('http://localhost:8088/woniusales')
    #     time.sleep(8)

    # def __init__(self, driver):
    #     self.driver = driver

    def __init__(self):
        self.driver = tool.get_webdriver()

    def do_login(self, username, password, verifycode):
        self.driver.find_element_by_id('username').clear()
        self.driver.find_element_by_id('username').send_keys(username)
        self.driver.find_element_by_id("password").clear()
        self.driver.find_element_by_id("password").send_keys(password)
        self.driver.find_element_by_id("verifycode").clear()
        self.driver.find_element_by_id("verifycode").send_keys(verifycode)
        self.driver.find_element_by_xpath("(//button[@type='button'])[5]").click()

    def test_login(self):
        self.do_login('admin', 'admin123', '0000')
        time.sleep(3)
        try:
            self.driver.find_element_by_link_text("注销")
            print("登录成功.")
        except:
            print("登录失败.")
