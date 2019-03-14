import requests,time,random,re,datetime,threading
class phpwindTest():
    def __init__(self):
        self.session=requests.session()#实例化一个会话
        self.verifycode=''#初始化动态验证码
        self.fid = random.randint(1, 3)# 随机获取帖子的页数
        self.data = {'fid': self.fid}#随机定义发帖版块
        self.nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')#获取当前系统时间
        self.atc_content=random.randint(1,999)#随机制定发帖内容
        self.quit_verify=''
        self.tid=''
    #登录系统
    def dologin(self):
        login='http://localhost/phpwind/upload/login.php?'
        login_data={'jumpurl':'http://localhost:8088/phpwind','step':2,'lgt':0,'pwuser':'admin','pwpwd':'admin','hideid':0,'cktime':31536000}
        login_res=self.session.post(url=login,data=login_data)
        actual=login_res.content.decode()
        expect='您已经顺利登录'
        if expect in actual:
            print('login successful!')
        else:
            print('login failed!')
        pattern_logout="(erasecookie&verify=)(.+?)(\">)"
        for result in re.finditer(pattern=pattern_logout,string=actual):
            self.quit_verify=result.group[2]
        print(self.quit_verify)
    #进入默认版块
    def add_before(self):
        before_url='http://localhost:8088/phpwind/thread.php'
        before_res=self.session.post(url=before_url,params=self.data)
        actual_before=before_res.content.decode()
        if '默认版块'in actual_before:
            print('进入版块成功')
        else:
            print('进入版块失败')
    # #选择发帖--获取动态验证码,用于发帖
    def choose_note(self):
        pub_url='http://localhost:8088/phpwind/post.php'
        pub_res=self.session.post(url=pub_url,params=self.data)
        pattern = "(name=\"verify\" value=\")(.+?)(\" />)"
        for result in re.finditer(pattern, pub_res.text):
            self.verifycode = str(result.group(2))
            # print(self.verifycode)
   #随机发帖--获取返回界面的tid
    def add_note(self):
        add_url='http://localhost:8088/phpwind/post.php'
        add_data={
                    'verify':self.verifycode,#动态验证码
                    'atc_title':'test'+self.nowTime,#帖子标题
                    'atc_content':self.atc_content,#帖子内容
                    'step':2,
                    'fid':self.fid,
                  }
        add_res=self.session.post(url=add_url,data=add_data)
        result=add_res.content.decode()
        if re.findall(pattern='发帖完毕',string=result):
            print('发帖 successful!')
        else:
            print('发帖 failed!')
        quit_pattern = "(tid=)(.+?)(\">)"
        for result_tid in re.finditer(pattern=quit_pattern, string=add_res.text):
            result = str(result_tid.group(2))
            self.tid=result
        # print(self.tid)
    #返回主界面--获取退出系统时需要的动态验证码
    def logout_before(self):
        log_url='http://localhost:8088/phpwind/read.php'
        param={'tid':self.tid}
        log_before=self.session.get(url=log_url,params=param)
        res=log_before.content.decode()
        quit_pattern="(action=quit&verify=)(.+?)(\">退出)"
        for result_quit in re.finditer(quit_pattern,res):
            result=str(result_quit.group(2))
            self.quit_verify=result
        # print(self.quit_verify)
    #退出系统
    def logout(self):
        logout_url='http://localhost:8088/phpwind/login.php'
        logout_data={'action':'quit','verify':self.quit_verify}
        logout_res=self.session.get(url=logout_url,params=logout_data)
        expect='您已经顺利退出网站'
        if expect in logout_res.content.decode():
            print('退出成功')
        else:
            print('退出失败')
    def start_test(self):
        for i in range(20):#每个线程运行20次
            self.dologin()
            self.choose_note()
            self.add_before()
            self.add_note()
            self.logout_before()
            self.logout()

if __name__ == '__main__':
    fa=phpwindTest()
    for i in range(50):
        t = threading.Thread(target=fa.start_test())
        t.start()
    


