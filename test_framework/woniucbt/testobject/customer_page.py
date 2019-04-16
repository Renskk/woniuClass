from selenium.webdriver.support.select import Select
from test_framework_43.woniucbt.common.tool import CommonTool as tool

class CustomerPage:
    def __init__(self):
        self.driver = tool.get_webdriver()

    def get_customerphone(self):
        return self.driver.find_element_by_id('customerphone')

    def get_customername(self):
        return self.driver.find_element_by_id('customername')

    def get_childsex(self):
        return Select(self.driver.find_element_by_id('childsex'))

    def get_childdate(self):
        self.driver.execute_script("document.getElementById('childdate').readOnly=false")
        return self.driver.find_element_by_id('childdate')

    def get_creditkids(self):
        self.driver.find_element_by_id('creditkids').clear()
        return self.driver.find_element_by_id('creditkids')

    def get_creditcloth(self):
        self.driver.find_element_by_id('creditcloth').clear()
        return self.driver.find_element_by_id('creditcloth')

    def get_add_button(self):
        return self.driver.find_element_by_xpath("(//button[@type='button'])[5]")

    def get_edit_button(self):
        return self.driver.find_element_by_xpath("(//button[@type='button'])[6]")

    def get_query_button(self):
        return self.driver.find_element_by_xpath("(//button[@type='button'])[7]")

    # 封装新增客户的操作
    def do_add(self, customerphone, customername, childsex, childdate, creditkids, creditcloth):
        self.get_customerphone().send_keys(customerphone)
        self.get_customername().send_keys(customername)
        self.get_childsex().select_by_visible_text(childsex)
        self.get_childdate().send_keys(childdate)
        self.get_creditkids().send_keys(creditkids)
        self.get_creditcloth().send_keys(creditcloth)
        self.get_add_button().click()