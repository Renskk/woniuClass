import uiautomator2 as u2
import time

d = u2.connect('127.0.0.1:62001')
print(d.device_info)

d.app_start('com.mobivans.onestrokecharge')
time.sleep(3)
s = d.session()
s(text='记一笔').click()
time.sleep(2)
s(text='支出').click()
time.sleep(2)
s(text='通讯').click()
s(resourceId='com.mobivans.onestrokecharge:id/keyb_btn_5').click()
s(resourceId='com.mobivans.onestrokecharge:id/keyb_btn_6').click()
s(resourceId='com.mobivans.onestrokecharge:id/add_et_remark').send_keys('Testing')
s(text='完成').click()

