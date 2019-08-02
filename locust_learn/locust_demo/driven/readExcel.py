# -*- coding: utf-8 -*-
import xlrd
class Excel(object):
    def __init__(self):
        self.data = xlrd.open_workbook(r'E:\work\pycharm\locustHomework\data\woniusalesLocust.xlsx')
        self.table = self.data.sheet_by_name('Sheet1')

        # get titles
        self.row = self.table.row_values(0)
        # get rows number
        self.rowNum = self.table.nrows
        # get columns number
        self.colNum = self.table.ncols
        # the current column
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


