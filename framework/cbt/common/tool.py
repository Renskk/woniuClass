from selenium import webdriver
import time

class CommonTool:

    driver = None     # 定义为类级变量

    def __init__(self):
        pass

    # @classmethod
    # def get_webdriver(cls):
    #     if cls.driver is None:
    #         cls.driver = webdriver.Chrome()
    #         cls.driver.get('http://localhost:8088/woniusales')
    #         cls.driver.maximize_window()
    #         cls.driver.set_page_load_timeout(10)
    #         time.sleep(3)
    #     return cls.driver

    # 根据browser参数，来决定在哪个浏览器上执行后续测试脚本
    @classmethod
    def get_webdriver(cls):
        if cls.driver is None:
            if cls.get_config('browser') == 'chrome':
                cls.driver = webdriver.Chrome()
            elif cls.get_config('browser') == 'firefox':
                cls.driver = webdriver.Firefox()
            elif cls.get_config('browser') == 'ie':
                cls.driver = webdriver.Ie()

            host = cls.get_config('host')
            port = cls.get_config('port')
            cls.driver.get('http://%s:%s/woniusales' % (host, port))
            cls.driver.maximize_window()
            cls.driver.set_page_load_timeout(10)
            time.sleep(3)
        return cls.driver

    # 读取global.conf文件内容，根据key返回value
    @staticmethod
    def get_config(key):
        with open('../data/global.conf') as file:
            content = file.readlines()
        for line in content:
            left = line.strip().split('=')[0]
            if left == key:
                return line.strip().split('=')[1]
        return ''
