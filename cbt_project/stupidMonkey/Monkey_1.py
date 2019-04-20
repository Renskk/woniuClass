# -*- coding: utf-8 -*-
import os,random,time,uiautomation,logging,threading
from selenium import webdriver
from pykeyboard import PyKeyboard
from pymouse import PyMouse
from PIL import ImageGrab
logging.basicConfig(level=logging.INFO,format='%(asctime)s-%(levelname)s-%(message)s',
                    filename='./data/'+time.strftime("%Y%m%d_%H%M%S.log"),filemode = 'w')
# logging.disable(logging.INFO)
class happyMonkey():
    def __init__(self):
        self.mouse = PyMouse()
        self.keyboard = PyKeyboard()
        self.dr = webdriver.Firefox()
        self.dr.get('http://192.168.7.20:8080/WoniuSales/')
        # os.popen(r'"C:\Program Files\Mozilla Firefox\firefox.exe" http://192.168.7.20:8080/WoniuSales/')
        self.Firefox_windows = uiautomation.WindowControl(ClassName='MozillaWindowClass')
        self.Firefox_windows.Maximize()
        self.Firefox_windows.SetTopmost()
        self.login_woniuSales()
        self.get_windows_resolution()
        # self.get_display()

    #登陆woniusales
    def login_woniuSales(self):
        self.dr.find_element_by_id('username').send_keys('admin')
        self.dr.find_element_by_id('password').send_keys('admin')
        self.dr.find_element_by_id('verifycode').send_keys('0000')
        self.dr.find_element_by_xpath("(//button[@type='button'])[5]").click()

    #获取窗口分辨率
    def get_windows_resolution(self):
        self.lx,self.ly,self.rx,self.ry = self.Firefox_windows.BoundingRectangle
        # print(self.lx,self.ly,self.rx,self.ry)
    #随机坐标移动
    def random_move(self):
        x = random.randint(self.lx,self.rx)
        y = random.randint(self.ry-94,self.ry)
        return (x,y)
    #鼠标左单击
    def click_left_mouse(self,x,y):
        # x,y = self.random_move()
        self.mouse.click(x=x,y=y,button=1,n=1)
        logging.info('click_left_mouse(%d,%d)'%(x,y))
    #鼠标左单击
    def click_right_mouse(self,x,y):
        # x,y = self.random_move()
        self.mouse.click(x=x,y=y,button=2,n=1)
        logging.info('click_right_mouse(%d,%d)'%(x,y))
    #鼠标左双击
    def click_double_left_mouse(self,x,y):
        # x,y = self.random_move()
        self.mouse.click(x=x,y=y,button=1,n=2)
        logging.info('click_double_left_mouse(%d,%d)'%(x,y))
    #鼠标中间键单击
    def click_middle_mouse(self,x,y):
        # x,y = self.random_move()
        self.mouse.click(x=x,y=y,button=3,n=1)
        logging.info('click_middle_mouse(%d,%d)'%(x,y))

    #检测有没有点出woniusales
    def detection_stupid_monkey(self):
        current_url = self.dr.current_url
        if 'WoniuSales' not in current_url:
            exit()
            logging.info('该程序进入其他网页，进程销毁！！！')

    def start_stupid_monkey(self,count,wiatime):
        for i in range(count):
            x, y = self.random_move()
            time.sleep(wiatime)
            num = random.randint(1, 80)
            self.detection_stupid_monkey()
            if num<=20:
                self.click_left_mouse(x,y)
            elif num<=40 and num>20:
                # self.click_right_mouse()
                pass
            elif num<=60 and num>40:
                self.click_double_left_mouse(x,y)
            elif num<=80 and num>60:
                self.click_middle_mouse(x,y)
            elif num<=90 and num>80:
                self.click_woniuslaes_module()
    #点击模块
    def click_woniuslaes_module(self):
        li = ['快捷导航','销售出库','销售出库','商品入库','库存查询','会员管理','销售报表']
        i = random.randint(0,len(li)-1)
        self.dr.find_element_by_link_text(li[i]).click()
        logging.info('切换为%s模块'%i)

    #截图
    def get_display(self):
        while True:
            time.sleep(2.333)
            now_time = time.strftime("%Y%m%d_%H%M%S.png")
            ImageGrab.grab().save(r'E:\work\pycharm\woniuCBT\stupidMonkey\screenshot\%s'%now_time)

if __name__ == '__main__':
    ha = happyMonkey()
    ha.start_stupid_monkey(20,2)
    # t = threading.Thread(target=ha.get_display())
    # t.setDaemon(True)
    # t.start()