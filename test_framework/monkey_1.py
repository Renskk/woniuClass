import time, os, random
from pymouse import PyMouse
from pykeyboard import PyKeyboard

class MonkeyTest:
    def __init__(self, waittime):
        self.mouse = PyMouse()
        self.keyboard = PyKeyboard()
        self.waittime = waittime

    # 实现随机移动的功能
    def random_move(self):
        x = random.randrange(10, 1390)
        y = random.randrange(50, 850)
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


if __name__ == '__main__':
    monkey = MonkeyTest(0.5)
    # monkey.start_app('calc.exe')
    os.system("taskkill /F /IM firefox.exe")
    time.sleep(2)
    monkey.start_app(r'"C:\Program Files (x86)\Mozilla Firefox 61\firefox.exe" http://www.baidu.com')

    monkey.start_test(30)
    os.system("taskkill /F /IM firefox.exe")