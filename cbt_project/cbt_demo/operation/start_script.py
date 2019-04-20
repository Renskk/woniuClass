# -*- coding: utf-8 -*-
from woniuCBT.cbt_demo.woniu_suite.open_browser import openBrowser
from woniuCBT.cbt_demo.woniu_suite.woniusales_login import woniuLogin
from woniuCBT.cbt_demo.woniu_suite.woniusales_sell import woniuSell



woniuLogin().login()
woniuSell().sell()