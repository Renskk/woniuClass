# 反射：通过字符串的方式来调用相应的对象或方法
from selenium.webdriver import ActionChains


class MyTest:
    var = 100000

    def get_name(self):
        print('蜗牛学院')

    def get_addr(self):
        print('成都孵化园')

    def set_value(self, value):
        print("你输入了：%s" % value)

    # def get_instance(self):
    #     return self
    #
    # def click(self):
    #     return MyTest

if __name__ == '__main__':
    my = MyTest()
    # my.get_instance().click().get_instance().click().click().get_name()
    # ActionChains().send_keys().click().double_click().click().click().send_keys().perform()

    # my.get_name()
    getattr(my, 'set_value')('Hello')
    print(hasattr(my, 'var'))
    print(getattr(my, 'var'))


# def testa():
#     def testb(value):
#         print("这是闭包内部的函数: " + value)
#
#     return testb
#
# testa()('Hello')