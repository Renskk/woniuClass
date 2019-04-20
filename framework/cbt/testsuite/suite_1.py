from test_framework_43.woniucbt.testcase.user import WoniuSalesUser
from test_framework_43.woniucbt.testcase.sell import WoniuSalesSell
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get('http://localhost:8088/woniusales')
time.sleep(3)

user = WoniuSalesUser(driver)
sell = WoniuSalesSell(driver)

user.test_login()
sell.test_barcode()