# -*- coding: utf-8 -*-
from meClass.cbt_project.cbt_demo.wn_suite.open_browser import openBrowser
from meClass.cbt_project.cbt_demo.wn_suite.wn_login import wnLogin
from meClass.cbt_project.cbt_demo.wn_suite.wn_sell import wnSell

wnLogin().login()
wnSell().sell()