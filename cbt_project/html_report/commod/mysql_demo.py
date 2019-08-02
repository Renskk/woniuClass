# -*- coding: utf-8 -*-
import pymysql,time
from pymysql.cursors import DictCursor

class HTMLReport:
    def __init__(self):
        pass
    def read_mysql(self,sql):
        con = pymysql.connect('localhost','root','','cbt_demo',charset='utf8')
        sor = con.cursor(DictCursor)
        sor.execute(sql)
        return sor.fetchall()

    def write_mysql(self,sql):
        con = pymysql.connect('localhost', 'root', '', 'cbt_demo', charset='utf8')
        sor = con.cursor()
        sql_time = time.strftime("%Y-%m-%d %H:%M:%S")
        sor.execute(sql)
        con.commit()
        sor.close()
        con.close()


    def write_report(self):
        with open('../report/template.html','r',encoding='utf8')as f:
            html_data = f.read()
        html_data = html_data.replace('$test-date','WoniuBoss TestReport')
        html_data = html_data.replace('$test-version','v1.0')
        try:
            html_data = html_data.replace('$pass-count',str(self.read_mysql(
                "SELECT count(*) as count FROM test WHERE test_result = '成功' GROUP BY version")[0]['count']))
        except:
            html_data = html_data.replace('$pass-count','0')
        try:
            html_data = html_data.replace('$fail-count', str(self.read_mysql(
                "SELECT count(*) as count FROM test WHERE test_result = '失败' GROUP BY version")[0]['count']))
        except:
            html_data = html_data.replace('$fail-count','0')
        try:
            html_data = html_data.replace('$error-count', str(self.read_mysql(
                "SELECT count(*) as count FROM test WHERE test_result = '异常' GROUP BY version")[0]['count']))
        except:
            html_data = html_data.replace('$error-count','0')
        html_data = html_data.replace('$last-time', str(self.read_mysql(
            "SELECT time FROM test order by id DESC limit 1")[0]['time']))
        data = self.read_mysql('SELECT * FROM test')
        # print(data)
        hdata = ''
        for i in range(len(data)):
            hdata += '<tr height="40">'
            hdata += '<td width="7%%">%s</td>'%data[i]['id']
            hdata += '<td width="9%%">%s</td>'%data[i]['modul']
            hdata += '<td width="9%%">%s</td>'%data[i]['test_type']
            hdata += '<td width="7%%">%s</td>'%data[i]['caseid']
            hdata += '<td width="20%%">%s</td>'%data[i]['case_text']
            if data[i]['test_result'] == '成功':
                hdata += '<td width="7%%" bgcolor = "palegreen">%s</td>'%data[i]['test_result']
            elif data[i]['test_result'] == '成功':
                hdata += '<td width="7%%" bgcolor = "lightgray">%s</td>' % data[i]['test_result']
            else:
                hdata += '<td width="7%%" bgcolor = "lightgoldenrodyellow">%s</td>' % data[i]['test_result']
            hdata += '<td width="16%%">%s</td>'%data[i]['time']
            hdata += '<td width="15%%">%s</td>'%data[i]['error']
            hdata += '<td width="10%%">%s</td>'%data[i]['screenshot']
            hdata += '</tr>'
        html_data = html_data.replace('$test-result',hdata)
        htime = time.strftime("%Y%m%d-%H%M")
        with open('../report/'+htime+'.html','w',encoding='utf8')as f:
            f.write(html_data)


if __name__ == '__main__':
    HTMLReport().write_report()