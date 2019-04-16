from test_framework_43.woniucbt.common.tool import CommonTool as tool
from test_framework_43.woniucbt.testobject.customer_page import CustomerPage
import time

class WoniuSalesCustomer:
    def __init__(self):
        self.driver = tool.get_webdriver()
        self.page = CustomerPage()

    def prepare(self):
        try:
            self.page.get_childsex().select_by_index(0)
        except:
            self.driver.find_element_by_link_text('会员管理').click()
            time.sleep(3)

    def do_add(self, customerphone, customername, childsex, childdate, creditkids, creditcloth):
        self.page.get_customerphone().send_keys(customerphone)
        self.page.get_customername().send_keys(customername)
        self.page.get_childsex().select_by_visible_text(childsex)
        self.page.get_childdate().send_keys(childdate)
        self.page.get_creditkids().send_keys(creditkids)
        self.page.get_creditcloth().send_keys(creditcloth)
        self.page.get_add_button().click()

    def test_add(self):
        self.prepare()
        self.do_add('13685818175', '张四', '男', '2018-12-13', '300', '200')
        # 断言略


