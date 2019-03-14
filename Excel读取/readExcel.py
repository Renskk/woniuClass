# -*- coding: utf-8 -*-
import xlrd,logging
logging.disable(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s-%(levelname)s-%(message)s')
class useXlrd(object):
    def __init__(self,excelAddr):
        self.data = xlrd.open_workbook(excelAddr) #获取文件地址
        self.table = self.data.sheet_by_name('Sheet1') #选择表格页面
        self.row = self.table.nrows #获取表格列数
        self.col = self.table.ncols #获取表格列数
    def readDate(self):
        table = self.table
        datas = []
        for i in range(1,self.row):
            data = {}
            for j in range(self.col):
                title = table.cell_value(0, j)
                value = table.cell_value(i, j)
                data[title] = value
            datas.append(data)
        return datas
    def test(self):
        new = self.readDate()
        for i in range(self.row-1):
            s={}
            datac = new[i]['参数']
            logging.debug('待参数字符串：%s'%datac)
            c=datac.split('\n')
            logging.debug('按换行符拆分参数字符串：%s'%c)
            for j in range(len(c)):
                b=c[j].split('=')
                logging.debug('按等号拆分参数字符串：%s'%b)
                s[b[0]]=b[1]
                logging.debug('拆解为字典的字符串：%s'%s)
            new[i]['参数']=s
        logging.debug('最终要求%s'%new)
        return new
if __name__ == '__main__':
    a = useXlrd(r'..\data\接口测试用例.xlsx')
    a.test()