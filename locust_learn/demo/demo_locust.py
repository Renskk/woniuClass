# -*- coding: utf-8 -*-
from locust import HttpLocust,TaskSet,task

class testLocust(TaskSet):
    @task
    def test1(self):
        self.logindata = [{'verifycode': '0000', 'resulte': 'login-fail', 'username': 'admin', 'password': 'admin'},
                          {'verifycode': '0000', 'resulte': 'login-pass', 'username': 'admin', 'password': 'adad'}]
        for i in range(len(self.logindata)):
            url = '/agileone/index.php/common/login'
            data = {'username':self.logindata[i]['username'],
                    'password':self.logindata[i]['password'],
                    'verifycode':self.logindata[i]['verifycode']}
            res = self.client.post(url,data)
            if self.logindata[i]['resulte'] in res.text:
                print('pass')
            else:
                print('fail')

        self.index = (self.index +1) % len(self.logindata)


class testWeb(HttpLocust):
    task_set = testLocust
    min_wait = 1000
    max_wait = 3000

#
#     @task
#     def test1(self):
#         self.index = 0
#         self.logindata = [['admin', 'admin'], ['admin', '123']]
#         url = '/agileone/index.php/common/login'
#         data = {'username':self.logindata[self.index][0],
#                 'password':self.logindata[self.index][1],'savelogin':'true'}
#         res = self.client.post(url,data)
#         print(res.text)
#         if 'successful' in res.text:
#             print('pass')
#         else:
#             print('fail')
#         self.index = (self.index +1) % len(self.logindata)
