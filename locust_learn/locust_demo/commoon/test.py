# -*- coding: utf-8 -*-
from locustHomework.driven.readExcel import Excel

print(Excel().next())
# logindata = Excel().next()
# # index = 0
# # for i in range(len(logindata)):
# #     url = '/agileone/index.php/common/login'
# #     data = {'username': logindata[i]['username'],
# #             'password': logindata[i]['password'],
# #             'verifycode': logindata[i]['verifycode']}
# #     print(logindata[i]['username'],logindata[i]['password'],logindata[i]['verifycode'])