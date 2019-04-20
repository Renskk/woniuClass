# -*- coding: utf-8 -*-
import uiautomator2 as u2


d = u2.connect('127.0.0.1:62001')
print(d.device_info)