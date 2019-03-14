# -*- coding: utf-8 -*-
import unittest,ddt,HTMLTestRunner,requests
from woniuBoss43TH.readExcel.readTest import useXlrd
excel = useXlrd(r'..\data\接口测试用例.xlsx')


@ddt.ddt
class product (unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    @ddt.data(*excel.test())
    def test1(self,da):
        if '登陆接口' in da['标题']:
            res = requests.get(da['接口地址'],da['参数'])
            self.assertIn(da['响应正文'], res.text)
        else:
            se = requests.session()
            se.post('http://localhost:8080/WoniuBoss2.0/log/userLogin',
                    {'userName': 'WNCD000', 'checkcode': '0000', 'userPass': 'Woniu123'})
            res = se.post(da['接口地址'],da['参数'])
            self.assertIn(da['响应正文'],res.text)



if __name__ == '__main__':
    suite=unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(product))
    with open('../report/测试报告.html','w',encoding='utf-8') as file:
        HTMLTestRunner.HTMLTestRunner(stream=file,verbosity=2).run(suite)