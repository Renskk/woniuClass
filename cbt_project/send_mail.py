import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# # 发件人地址，收件人地址，邮件服务器地址，账号和密码
# sender = 'xxxx@woniuxy.com'   # 发送邮箱
# receivers = ['xxxxx@woniuxy.com']  # 接收邮箱
#
# # 设置邮件正文
# # 三个参数：第一个为内容，第二个plain设置文本格式，第三个utf-8设置编码
# message = MIMEText('<p style="color: blue; font-size: 30px">'
#                    '这是一封来自Python发送的测试邮件的内容...</p>',
#                    'html', 'utf-8')
# # 设置邮件标题
# message['Subject'] = Header('二封Python发送的邮件', 'utf-8')
#
# try:
#     smtpObj = smtplib.SMTP()
#     # 输入邮件服务器地址，账号和密码
#     smtpObj.connect('mail.xxxxx.com', 25)
#     smtpObj.login(user='xxx@xx.com', password='xxxx')
#
#     # 正式发送邮件
#     smtpObj.sendmail(sender, receivers, message.as_string())
#     print("邮件发送成功")
# except smtplib.SMTPException:
#     print("Error: 无法发送邮件")



# 如何发送带附件的邮件
sender = 'xxxxx@woniuxy.com'  # 发送邮箱
receivers = 'xxxx@woniuxy.com'  # 接收邮箱

# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
# message = MIMEText('<p style="color: red; font-size: 30px">这是一封来自Python发送的测试邮件的内容...</p>', 'html', 'utf-8')
# message['Subject'] = Header('一封Python发送的邮件', 'utf-8')

msg = MIMEMultipart()
msg['Subject'] = '一封Python发送的邮件'
msg['From'] = sender
msg['To'] = receivers

content = MIMEText('<p style="color: red; font-size: 20px">这是一封来自Python发送的测试邮件的内容...</p>', 'html', 'utf-8')
# content = '这是一封来自Python发送的测试邮件的内容...'
msg.attach(content)

attachment = MIMEApplication(open('D:/6.jpg', 'rb').read())
attachment.add_header('Content-Disposition', 'attachment', filename='woniu.jpg')
msg.attach(attachment)

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect('mail.xxxxx.com', '25')
    smtpObj.login(user='xxx@xx.com', password='xxxxx')
    smtpObj.sendmail(sender, receivers, str(msg))
    smtpObj.quit()
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")