from appium import webdriver
import time, os, random
from appium.webdriver.common.touch_action import TouchAction


def input_pay(driver, number):
    for c in str(number):
        driver.find_element_by_id('keyb_btn_%s' % c).click()
        time.sleep(0.5)

desired_caps = {}       # 定义webdriver的兼容性设置字典对象
desired_caps['platformName'] = 'Android'    # 指定测试Android平台
desired_caps['platformVersion'] = '4.4.2'   # 指定移动端的版本号
desired_caps['deviceName'] = 'Appium'       # 指定设备名称
# desired_caps['automationName'] = 'uiautomator2'
desired_caps['appPackage'] = 'com.mobivans.onestrokecharge'  # 指定要启动的包
desired_caps['appActivity'] = 'com.stub.stub01.Stub01' # 指定启动的主类程序
desired_caps['unicodeKeyboard'] = 'True'    # 使用中文输入法
desired_caps['udid'] = '127.0.0.1:62001'    # 指定模拟器设备编号(adb devices输出结果)
desired_caps['noReset'] = 'True'            # 不重置应用程序的状态，默认为false

driver = webdriver.Remote('http://127.0.0.1:5000/wd/hub', desired_caps)
time.sleep(3)

driver.find_element_by_name('记一笔').click()
time.sleep(2)

driver.find_element_by_id('com.mobivans.onestrokecharge:id/add_txt_Pay').click()

# 从上往下，按层次关系找
parent = driver.find_element_by_id('com.mobivans.onestrokecharge:id/add_rv_cateGrid')
cate_list = parent.find_elements_by_class_name('android.widget.TextView')
rand_index = random.randrange(0, len(cate_list)-2)
cate_list[rand_index].click()
cate_type = cate_list[rand_index].text

# cate_list = driver.find_elements_by_id('com.mobivans.onestrokecharge:id/item_cate_text')

driver.find_element_by_id('add_et_remark').send_keys('支出类型：' + cate_type)
pay_number = random.randint(10, 9999)
input_pay(driver, pay_number)

driver.find_element_by_id('com.mobivans.onestrokecharge:id/keyb_btn_finish').click()

# 对新增的支出项进行断言：从父元素找下级，找第一个
detail_list = driver.find_elements_by_id('com.mobivans.onestrokecharge:id/account_item_detail')
target_text = detail_list[0].find_element_by_id('account_item_txt_remark').text
target_pay = detail_list[0].find_element_by_id('account_item_txt_money').text
if target_text == '支出类型：' + cate_type and target_pay == str(pay_number*-1):
    print('新增成功.')
else:
    print("新增失败.")

# 对新增的支出项进行断言：直接根据输入的文本找对应的元素
try:
    driver.find_element_by_name('支出类型：' + cate_type)
    driver.find_element_by_name(str(pay_number*-1))
    print("新增成功.")
except:
    print("新增失败.")