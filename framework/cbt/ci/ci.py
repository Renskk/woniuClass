# 利用和Python结合命令，文件系统操作，Ant，Tomcat等实现持续集成
import time, os, threading, shutil, requests
from selenium import webdriver
from test_framework_43.woniucbt.ci.woniusales_report import WoniuSalesTest
from test_framework_43.woniucbt.ci.html_report import HTMLReporter

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

class CI:
    def __init__(self, version):
        self.version = version

    # 从SVN当中获取最新版本的源代码
    def svn(self):
        try:
            os.listdir('F:/WoniuSales')
            os.system('svn update F:/WoniuSales')
            print("已经从SVN库中Update到最新版本.")
        except:
            os.system('svn checkout https://localhost:8443/svn/WoniuSales F:\WoniuSales --username=denny --password=123456')
            print("已经从SVN库中Checkout到最新版本.")

    # 利用ant完成构建
    def ant(self):
        if os.path.exists('F:/WoniuSales/build.xml'):
            os.system('ant -f F:/WoniuSales/build.xml')
            print("Ant构建woniusales.war包成功.")
        else:
            self.svn()
            self.ant()

    # 部署到Tomcat的webapps目录下
    def deploy(self):
        # 删除之前的版本
        try:
            # os.system(r'rd /S /Q C:\Tools\Tomcat8.0\webapps\woniusales')
            shutil.rmtree(r'C:\Tools\Tomcat8.0\webapps\woniusales')
            os.system(r'del /S /Q C:\Tools\Tomcat8.0\webapps\woniusales.war')
            # os.system(r'copy F:\WoniuSales\woniusales.war C:\Tools\Tomcat8.0\webapps\woniusales.war')
            shutil.move(r'F:\WoniuSales\woniusales.war', r'C:\Tools\Tomcat8.0\webapps\woniusales.war')
            print("成功将woniusales.war包移动到Tomcat中.")
            time.sleep(5)
        except:
            print("部署失败，请确认原因.")   # 正式的企业环境中，此处可以发短信了

    # 如果Tomcat没有启动，则启动它
    def start(self):
        # 利用tasklist(ps -ef)来查找Tomcat的进程java.exe
        # 访问网址(requests)，确认网址内容
        # 判断是否在webapps目录下生成了woniusales目录
        # 利用socket判断tomcat端口是否被占用
        try:
            resp = requests.get('http://localhost:8088/woniusales/')
            print("部署已经完成，可以开始测试了.")
        except:
            os.system(r'C:\Tools\Tomcat8.0\bin\startup.bat')
            time.sleep(15)
            print("Tomcat已经成功启动，即将进行测试.")

    # 发送测试报告邮件
    def email(self):
        # 发件人地址，收件人地址，邮件服务器地址，账号和密码
        sender = 'student@woniuxy.com'   # 发送邮箱
        receivers = ['dengqiang@woniuxy.com']  # 接收邮箱

        # 设置邮件正文
        # 三个参数：第一个为内容，第二个plain设置文本格式，第三个utf-8设置编码

        # 打开测试报告的HTML正文，并作为邮件正文发送
        ymd = time.strftime('%Y%m%d')
        report_name = report_name = './report/%s/report_%s.html' % (ymd, self.version)
        with open(report_name, encoding='utf-8') as file:
            content = file.read()

        message = MIMEText(content, 'html', 'utf-8')
        # 设置邮件标题
        message['Subject'] = Header('这是版本%s的测试报告' % self.version, 'utf-8')

        try:
            smtpObj = smtplib.SMTP()
            # 输入邮件服务器地址，账号和密码
            smtpObj.connect('mail.woniuxy.com', 25)
            smtpObj.login(user='student@woniuxy.com', password='Student123')

            # 正式发送邮件
            smtpObj.sendmail(sender, receivers, message.as_string())
            print("邮件发送成功")
        except smtplib.SMTPException:
            print("Error: 无法发送邮件")

    # 调用测试脚本，开始执行测试
    def test(self):
        # resp = requests.get('http://localhost:8088/woniusales/')
        # resp.encoding = 'utf-8'
        # if '蜗牛进销存' in resp.text:
        #     print("测试成功.")
        # else:
        #     print("测试失败.")
        #
        # driver = webdriver.Firefox()
        # driver.get('http://localhost:8088/woniusales')

        test = WoniuSalesTest()
        test.test_login_ui()
        test.test_login_http()
        time.sleep(5)

        report = HTMLReporter(self.version)
        report.generate_report()


if __name__ == '__main__':
    ci = CI('1.1.6')
    # ci.svn()
    # ci.ant()
    # ci.deploy()
    # ci.start()
    ci.test()
    ci.email()