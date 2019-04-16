import time, os, threading
import uiautomator2 as u2

class AndroidCloud:
    def __init__(self):
        pass

    def get_devices(self):
        output = os.popen('adb devices').read().strip()
        list = output.split('\n')
        device_list = []
        for i in range(1, len(list)):
            device_list.append(list[i].split('\t')[0])
        return device_list

    def start_test(self, udid):
        d = u2.connect(udid)
        d.app_start('com.mobivans.onestrokecharge')
        time.sleep(5)
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

if __name__ == '__main__':
    ac = AndroidCloud()
    device_list = ac.get_devices()
    for udid in device_list:
        threading.Thread(target=ac.start_test,args=(udid,)).start()