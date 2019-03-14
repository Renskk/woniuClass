# -*- coding: utf-8 -*-
import os
from woniuBoss43TH.readExcel.readTest import useXlrd


#============= excel文件位置 ===============
excel = useXlrd(r'..\data\接口测试用例.xlsx')

#============= 启动执行脚本 =================
# os.popen('python ..\drive\driver.py')