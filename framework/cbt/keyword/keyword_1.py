import time, os, random
from selenium import webdriver

class KeywordDriven:
    def __init__(self):
        self.driver = webdriver.Firefox()

    def open(self, url):
        self.driver.get(url)

    def wait(self, second):
        time.sleep(int(second))

    def input(self, identify, text):
        self.find_element(identify).send_keys(text)

    def click(self, identify):
        self.find_element(identify).click()

    def check(self, identify, text):
        if self.find_element(identify).text == text:
            print('测试成功')
        else:
            print("测试失败")

    def find_element(self, identify):
        by = identify.split('=')[0]
        value = identify.split('=', 1)[1]
        if by == 'id':
            return self.driver.find_element_by_id(value)
        elif by == 'xpath':
            return self.driver.find_element_by_xpath(value)
        elif by == 'linktext':
            return self.driver.find_element_by_link_text(value)

    def keyword_run(self, keyword_file):
        with open(keyword_file, encoding='utf-8') as file:
            line_list = file.readlines()

        for line in line_list:
            temp_list = line.split(',')
            command = line.split(',')[0]
            identify = line.split(',')[1]
            if len(temp_list) == 2:
                getattr(self, command)(identify)
            if len(temp_list) == 3:
                text = line.split(',')[2]
                getattr(self, command)(identify, text)

if __name__ == '__main__':
    keyword = KeywordDriven()
    keyword.keyword_run('./keyword.txt')


    # 如果关键字里面需要使用中文，比如: 打开，输入，单击，检查等，则通过使用字典将中文和英文方法名进行关联即可.
    # dict = {'打开':'open', '输入':'input'}