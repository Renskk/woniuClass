# -*- coding: utf-8 -*-
import re


with open('./data/20190403_113634.log')as f:
    dataline = f.read()
data = dataline.strip().split('\n')
regex = re.compile('\(.+\)')
for i in range(len(data)):
    mo = regex.search(data[i]).group()
    x,y = mo.replace('(','').replace(')','')
    print(x)
    # print(type(da))

# regex = re.compile('\(.*?\)')
# mo=regex.search(data[0]).group()
# print(mo)