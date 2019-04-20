import time, os, random
from pymouse import PyMouse
from pykeyboard import PyKeyboard
from test_framework_43.image_match import ImageMatch

# 基于图像识别技术封装的自动化测试框架的接口
class ImageTest:
    def __init__(self, folder):
        self.mouse = PyMouse()
        self.keyboard = PyKeyboard()
        self.matcher = ImageMatch()
        self.folder = folder

    def click(self, image):
        x, y = self.matcher.find_image(self.folder + image)
        self.mouse.click(x, y)
        print('在[%d, %d]的位置，针对%s图片，单击.' % (x, y, image))

    def input(self, image, string):
        x, y = self.matcher.find_image(self.folder + image)
        print("当前坐标%d, %d" % (x, y))
        self.mouse.click(x, y)
        self.keyboard.type_string(string)
        print('在[%d, %d]的位置，针对%s图片，输入: %s' % (x, y, image, string))

    def start_app(self, command):
        os.system("start /b " + command)
        print("启动应用程序成功.")
        time.sleep(3)

    def exists(self, image):
        x, y = self.matcher.find_image(self.folder + image)
        if (x, y) != (-1, -1):
            return True
        else:
            return False

if __name__ == '__main__':
    it = ImageTest('./screenshot/')
    it.start_app(r'"C:\Program Files (x86)\Mozilla Firefox 61\firefox.exe" http://localhost:8088/woniusales')
    time.sleep(10)
    it.input('username.png', 'admin')
    it.input('password.png', 'admin123')
    it.input('verifycode.png', '0000')
    it.click('dologin.png')
    time.sleep(3)
    if it.exists('checklogin.png'):
        print("测试登录成功.")
    else:
        print("测试登录失败.")