import os, shutil, time
from selenium import webdriver
import threading

# 首先需要配置好svn的环境变量，ant的环境变量，build.xml可正常工作
def svn_checkout():
    shutil.rmtree('F:/WoniuSales')  # 删除之前checkout出来的源代码
    time.sleep(3)
    # 利用svn命令将最新版本源代码进行checkout
    output = os.popen('svn checkout https://localhost:8443/svn/WoniuSales F:/WoniuSales --username denny --password 123456').read()
    output = output[-10:-2]
    version = output.split(" ")[1]
    # 为了更加频繁地进行持续集成，可以解析本次checkout的最新版本号，下一次运行时可以通过以下命令来进行更新，而不需要每一次都整个项目checkout
    # svn diff -r 版本号:HEAD --summarize https://localhost:8443/svn/WoniuSales
    print('当前最新版本为：' + str(version))
    time.sleep(3)

# 利用ant命令进行版本构建，最终生成war包，并删除之前版本的war和目录，复制最新版本的war到Tomcat下
def build_copy():
    os.system('ant -buildfile F:/WoniuSales/build.xml')
    time.sleep(3)
    os.remove('C:/Tools/Tomcat8.0/webapps/woniusales.war')
    shutil.rmtree('C:/Tools/Tomcat8.0/webapps/woniusales')
    time.sleep(3)
    shutil.copy('F:/WoniuSales/woniusales.war', 'C:/Tools/Tomcat8.0/webapps/woniusales.war')
    time.sleep(3)

# 启动Tomcat，此处必须另起一个线程，否则Tomcat会阻塞主线程
def start_run():
    os.system(r'C:\Tools\Tomcat8.0\bin\shutdown.bat')
    time.sleep(3)
    os.system(r'C:\Tools\Tomcat8.0\bin\startup.bat')

# 正常进行UI自动化和接口自动化代码，并生成测试报告（细节略）
def test_login():
    driver = webdriver.Firefox()
    driver.get('http://localhost:8088/woniusales')
    time.sleep(8)
    driver.find_element_by_id('username').clear()
    driver.find_element_by_id('username').send_keys("admin")
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys('admin123')
    driver.find_element_by_id("verifycode").clear()
    driver.find_element_by_id("verifycode").send_keys("0000")
    driver.find_element_by_xpath("(//button[@type='button'])[5]").click()
    time.sleep(3)

if __name__ == '__main__':
    svn_checkout()
    build_copy()
    threading.Thread(target=start_run).start()
    time.sleep(20)  # 为了给Tomcat启动时间，建议将些时间设置得大一些
    test_login()
