# 实现Monkey测试的原样回放，以实现类似于Android ADB Monkey命令中的-s seed.

import time, os, random
from pymouse import PyMouse
from pykeyboard import PyKeyboard

class MonkeyReplay:
    def __init__(self, waittime):
        self.mouse = PyMouse()
        self.keyboard = PyKeyboard()
        self.waittime = waittime
        self.logname = time.strftime("monkey_%Y%m%d_%H%M%S.txt")

    # 实现随机移动的功能
    def random_move(self):
        x = random.randrange(50, 1400)
        y = random.randrange(50, 850)
        self.mouse.move(x, y)
        print("移动到[%d, %d]位置." % (x, y))
        return (x, y)

    # 实现单击功能
    def random_click(self):
        x, y = self.random_move()
        self.mouse.click(x, y)
        print("在[%d, %d]处：单击." % (x, y))
        self.write_log(f"click,{x},{y}")
        time.sleep(self.waittime)

    # 实现随机输入
    def random_input(self):
        x, y = self.random_move()
        # 定义26个大写，小写，10个数字，部分符号，存入4个列表中  ['A', 'B', 'c', 'd', '1', '2', '%']
        content = ["Woniuxy", "123456", "Good Night", "Tomorrow Better!",
                   "Testing", "666667788", "123.45", "2018-08-06", "12", "8", "你好"]
        string = random.sample(content, 1)[0]
        self.keyboard.type_string(string)
        print("在[%d, %d]处输入：%s." % (x, y, string))
        self.write_log(f"input,{x},{y},{string}")
        time.sleep(self.waittime)

    # 将操作及位置等数据记录到文件中
    def write_log(self, content):
        with open("./data/" + self.logname, "a+", encoding='utf-8') as file:
            file.write(content + '\n')

    # 启动应用程序
    def start_app(self, path):
        os.system("start /b " + path)
        os.popen(path)
        print("启动应用程序成功.")
        time.sleep(3)

    # 执行随机事件
    def start_test(self, count):
        for i in range(count):
            number = random.randint(1, 50)
            if number <= 30:
                self.random_click()
            else:
                self.random_input()

    # 读取Monkey日志文件并执行相应事件序列
    def start_replay(self, logname):
        with open("./data/" + logname) as file:
            line_list = file.readlines()

        for line in line_list:
            event = line.strip().split(',')[0]
            x = int(line.strip().split(',')[1])
            y = int(line.strip().split(',')[2])
            if event == 'input':
                string = line.strip().split(',')[3]

            if event == 'click':
                self.mouse.click(x, y)
                print("在[%d, %d]处：单击." % (x, y))
                time.sleep(self.waittime)
            elif event == 'input':
                self.mouse.move(x, y)
                self.keyboard.type_string(string)
                print("在[%d, %d]处输入：%s." % (x, y, string))
                time.sleep(self.waittime)


if __name__ == '__main__':
    replay = MonkeyReplay(0.5)
    replay.start_app("calc.exe")
    # replay.start_test(15)
    replay.start_replay('monkey_20190403_111538.txt')