import os, time, random, requests
from selenium import webdriver
from test_framework_43.woniucbt.ci.html_report import HTMLReporter

class WoniuSalesTest:
    def __init__(self):
        self.report = HTMLReporter('1.1.6')
        self.session = requests.session()
        self.driver = webdriver.Firefox()
        self.driver.get('http://localhost:8088/woniusales')
        time.sleep(8)

    # def write_report(self,caseid, casetitle, result, error, screenshot):
    #     self.report.write_result(module='登录')

    def test_login_ui(self):
        try:
            self.driver.find_element_by_id('username').clear()
            self.driver.find_element_by_id('username').send_keys("admin")
            self.driver.find_element_by_id("password").clear()
            self.driver.find_element_by_id("password").send_keys('admin123')
            self.driver.find_element_by_id("verifycode").clear()
            self.driver.find_element_by_id("verifycode").send_keys("0000")
            self.driver.find_element_by_xpath("(//button[@type='button'])[5]").click()
            time.sleep(3)

            if self.driver.find_element_by_link_text("注销"):
                self.report.write_result("登录", 'UI自动化', 'Login-001', '登录WoniuSales')
            else:
                self.report.write_result("登录", 'UI自动化', 'Login-001', '登录WoniuSales', result='失败',
                                         error='断言失败', screenshot=self.report.capture_screenshot())

        except Exception as e:
            self.report.write_result("登录", 'UI自动化', 'Login-001', '登录WoniuSales', result='异常',
                                     error=e, screenshot=self.report.capture_screenshot())

    def test_login_http(self):
        try:
            url = 'http://localhost:8088/woniusales/user/login'
            data = {'username':'admin', 'password':'admin123', 'verifycode':'0000'}
            resp = self.session.post(url=url, data=data)
            if resp.text == 'login-pass':
                self.report.write_result("登录", '接口自动化', 'Login-002', '登录WoniuSales')
            else:
                self.report.write_result("登录", '接口自动化', 'Login-002', '登录WoniuSales', result='失败',
                                         error='断言失败')
        except Exception as e:
            self.report.write_result("登录", '接口自动化', 'Login-002', '登录WoniuSales', result='异常',
                                     error=e)

    # username=admin&password=admin123&verifycode=0000
    def string_to_dict(self, string):
        dict = {}
        list = string.split('&')
        for item in list:
            key = item.split('=')[0]
            value = item.split('=')[1]
            dict[key] = value
        return dict

if __name__ == '__main__':
    wst = WoniuSalesTest()
    wst.test_login_ui()
    wst.test_login_http()