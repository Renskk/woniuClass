# -*- coding: utf-8 -*-
import xlrd
from locust import HttpLocust, TaskSet, task

class Excel(object):
    def __init__(self):
        self.data = xlrd.open_workbook('woniusalesLocust.xlsx')
        self.table = self.data.sheet_by_name('Sheet1')
        self.row = self.table.row_values(0)
        self.rowNum = self.table.nrows
        self.colNum = self.table.ncols
        self.curRowNo = 1

    def next(self):
        r = []
        while self.hasNext():
            s = {}
            col = self.table.row_values(self.curRowNo)
            i = self.colNum
            for x in range(i):
                s[self.row[x]] = col[x]
            r.append(s)
            self.curRowNo += 1
        return r

    def hasNext(self):
        if self.rowNum == 0 or self.rowNum <= self.curRowNo:
            return False
        else:
            return True

class testLocust(TaskSet):

    @task
    def test1(self):
        self.logindata = Excel().next()
        for i in range(len(self.logindata)):
            url = '/WoniuSales/user/login'
            data = {'username':self.logindata[i]['username'],
                    'password':self.logindata[i]['password'],
                    'verifycode':self.logindata[i]['verifycode']}
            with self.client.post(url,data,catch_response=True) as res:
            # print(res.text)
            # print(res.success())
            # print(self.logindata[i]['resulte'])
                if self.logindata[i]['resulte'] == res.text:
                    res.success()
                else:
                    res.failure('fail')


class testWeb(HttpLocust):
    task_set = testLocust
    host = 'http://192.168.7.20:8080'
    min_wait = 1000
    max_wait = 3000


