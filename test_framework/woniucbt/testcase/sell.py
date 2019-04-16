import os, time, random, requests
from selenium import webdriver
from test_framework_43.woniucbt.common.tool import CommonTool as tool

class WoniuSalesSell:
    # def __init__(self):
    #     self.driver = webdriver.Firefox()
    #     self.driver.get('http://localhost:8088/woniusales')
    #     time.sleep(8)

    # def __init__(self, driver):
    #     self.driver = driver

    def __init__(self):
        self.driver = tool.get_webdriver()

    def do_barcode(self, barcode):
        self.driver.find_element_by_id('barcode').clear()
        self.driver.find_element_by_id('barcode').send_keys(barcode)
        self.driver.find_element_by_xpath("(//button[@type='button'])[5]").click()

    def test_barcode(self):
        self.do_barcode('6955203657732')
        goods_list = self.driver.find_element_by_id("goodslist")
        tr_list = goods_list.find_elements_by_tag_name("tr")
        if len(tr_list) == 1:
            print('扫码数量正确.')
        else:
            print('扫码数量错误.')