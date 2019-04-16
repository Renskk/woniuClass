import time, os, random, uiautomation
from pymouse import PyMouse
from pykeyboard import PyKeyboard
from PIL import ImageGrab
import threading

class MonkeyTest:
    def __init__(self, waittime):
        self.mouse = PyMouse()
        self.keyboard = PyKeyboard()
        self.waittime = waittime
        self.left_top_x = 0
        self.left_top_y = 0
        self.right_bottom_x = 0
        self.right_bottom_y = 0

    # 实现随机移动的功能
    def random_move(self):
        x = random.randrange(self.left_top_x+20, self.right_bottom_x-20)
        y = random.randrange(self.left_top_y+100, self.right_bottom_y-20)
        self.mouse.move(x, y)
        print("移动到[%d, %d]位置." % (x, y))
        return (x, y)

    # 实现单击功能
    def random_click(self):
        x, y = self.random_move()
        self.mouse.click(x, y)
        print("在[%d, %d]处：单击." % (x, y))
        time.sleep(self.waittime)

    # 实现双击功能
    def random_double_click(self):
        x, y = self.random_move()
        self.mouse.click(x, y, n=2)
        print("在[%d, %d]处：双击." % (x, y))
        time.sleep(self.waittime)

    # 实现右键功能
    def random_right_click(self):
        x, y = self.random_move()
        self.mouse.click(x, y, button=2)
        print("在[%d, %d]处：右键." % (x, y))
        time.sleep(self.waittime)

    # 实现随机输入
    def random_input(self):
        x, y = self.random_move()
        # 定义26个大写，小写，10个数字，部分符号，存入4个列表中  ['A', 'B', 'c', 'd', '1', '2', '%']
        content = ["Woniuxy", "123456", "Good Night", "Tomorrow Better!",
                   "Testing", "666667788", "123.45", "2018-08-06", "12", "8", "你好"]
        string = random.sample(content, 1)[0]
        self.keyboard.type_string(string)
        print("在[%d, %d]处输入：%s." %(x, y, string))
        time.sleep(self.waittime)

    # 控制字符的输入
    def random_special(self):
        x, y = self.random_move()
        key_list = [self.keyboard.enter_key, self.keyboard.backspace_key, self.keyboard.alt_key,
                    self.keyboard.control_key, self.keyboard.up_key, self.keyboard.down_key, self.keyboard.left_key]
        keys_list = [[self.keyboard.control_key, 'c'], [self.keyboard.alt_key, self.keyboard.function_keys[5]],
                     [self.keyboard.control_key, 'v'],
                     [self.keyboard.control_key, self.keyboard.shift_key, self.keyboard.space_key]]
        number = random.randint(1, 20)
        if number <= 10:
            key_code = random.choice(key_list)
            self.keyboard.press_key(key_code)
            self.keyboard.release_key(key_code)
            print("在[%d, %d]处进行按键. %s" % (x, y, key_code))
        else:
            keys_code = random.choice(keys_list)
            self.keyboard.press_keys(keys_code)
            print("在[%d, %d]处进行按键. %s" % (x, y, keys_code))
        time.sleep(self.waittime)

    # 启动应用程序
    def start_app(self, path):
        os.system("start /b " + path)
        os.popen(path)
        print("启动应用程序成功.")
        time.sleep(3)

    # 检查进程是否存在
    def check_process(self, pname):
        result = os.popen("tasklist | findstr %s" % pname).read()
        if not pname in result:
            print("进程已经结束.")
            exit(0)

    # 执行随机事件
    def start_test(self, count):
        for i in range(count):
            number = random.randint(1, 100)
            if number <= 20:
                self.random_click()
            elif number <= 40:
                self.random_double_click()
            elif number <= 60:
                self.random_right_click()
            elif number <= 80:
                self.random_input()
            else:
                self.random_special()

            self.check_process("firefox.exe")


    # 后台截图
    def capture_screen(self):
        while True:
            now_time = time.strftime("%Y%m%d_%H%M%S.png")
            ImageGrab.grab().save('./screenshot/' + now_time)
            time.sleep(3)


if __name__ == '__main__':
    monkey = MonkeyTest(0.5)
    # monkey.start_app('calc.exe')
    os.system("taskkill /F /IM firefox.exe")
    time.sleep(2)
    monkey.start_app(r'"C:\Program Files (x86)\Mozilla Firefox 61\firefox.exe" http://localhost:8088/woniusales')
    time.sleep(5)
    firefox_window = uiautomation.WindowControl(ClassName="MozillaWindowClass")
    firefox_window.Maximize()   # 最大化窗口
    firefox_window.SetTopmost()   # 设置置顶
    x1, y1, x2, y2 = firefox_window.BoundingRectangle
    monkey.left_top_x, monkey.left_top_y, monkey.right_bottom_x, monkey.right_bottom_y = x1, y1, x2, y2

    time.sleep(3)
    monkey.start_test(30)

    # 后台启动截图功能
    t = threading.Thread(target=monkey.capture_screen)
    t.setDaemon(True)   # 让子线程作为守护线程运行，并随着主线程的结束而结束
    t.start()
    # t.join()          # 将子线程合并到主线程，那么主线程的结束条件一定是子线程全部结束以后，主线程才能结束(一个线程)

    os.system("taskkill /F /IM firefox.exe")