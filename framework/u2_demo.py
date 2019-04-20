import uiautomator2 as u2
import time

d = u2.connect('127.0.0.1:62001')
print(d.device_info)

d.app_start('com.miui.calculator')
time.sleep(3)

d(resourceId='com.miui.calculator:id/btn_5').click()
d(resourceIdMatches='.*btn_plus').click()
d(resourceId='com.miui.calculator:id/btn_7').click()
d(description='等于').click()

