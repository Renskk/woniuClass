from test_framework_43.woniucbt.testcase.user import WoniuSalesUser
from test_framework_43.woniucbt.testcase.sell import WoniuSalesSell
from test_framework_43.woniucbt.testcase.customer import WoniuSalesCustomer
from selenium import webdriver
from test_framework_43.woniucbt.common.tool import CommonTool as tool
import time

user = WoniuSalesUser()
sell = WoniuSalesSell()
customer = WoniuSalesCustomer()

user.test_login()
# sell.test_barcode()
customer.test_add()

# user.do_login('admin', 'admin123', '0000')
# sell.do_barcode('6955203657732')
# sell.do_barcode('6955203651099')
# sell.do_barcode('6955203660510')