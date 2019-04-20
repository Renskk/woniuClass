# -*- coding: utf-8 -*-
import requests,os
class guest():
    def __init__(self):
        self.read_data()
    def read_data(self):
        file = os.path.abspath('.\\guest_data.csv')
        with open(file,'r') as f :
            result = f.readlines()#读取表中所有的数据
            col = result[0].strip().split(',')#读取表中第一行数据
            cols = len(col)#获取表中数据列数
            rows = len(result)#获取表中数据行数
            list = []
            for i in range (1,rows):
                value = result[i].strip().split(',')
                dict = {}
                for j in range(cols):
                    dict[col[j]] = value[j]
                list.append(dict)
        return list
    def test_guest(self):
        data = self.read_data()
        for i in range(len(data)):
            pam  = {'eid':data[i]['eid']}
            print(pam)
            re = requests.get('http://127.0.0.1:8000/api/get_event_list/',params=pam)
            try:
                if int(data[i]['status']) == re.json()['status']:
                    print('测试通过')
                else:
                    print('测试失败')
            except: print('某些莫名错误')


if __name__ == '__main__':
    guest().test_guest()