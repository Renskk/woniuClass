import os, time, random, pymysql
from pymysql.cursors import DictCursor
from PIL import ImageGrab


class HTMLReporter:
    def __init__(self, version):
        self.version = version

    def generate_report(self):
        conn = pymysql.connect(user='root', passwd='123456', host='localhost', db='test', charset='utf8')
        # cursor = conn.cursor()
        # 使用以字典类型返回结果集的游标
        cursor = conn.cursor(DictCursor)
        sql = "select * from report where version='%s'" % self.version
        cursor.execute(sql)
        result_list = cursor.fetchall()

        testtime = result_list[0]['testtime']
        lasttime = result_list[len(result_list)-1]['testtime']

        # 打开模板文件，进行模板变量的替换，并保存到报告文件中
        with open('./report/template.html', encoding='utf-8') as file:
            content = file.read()

        content = content.replace('$test-date', str(testtime))
        content = content.replace('$last-time', str(lasttime))
        content = content.replace('$test-version', self.version)

        # 针对当前版本，获取成功，异常和失败的数量
        sql = "select result, count(*) as count from report where version='%s' group by result" % self.version
        cursor.execute(sql)
        count_list = cursor.fetchall()
        error_count, pass_count, fail_count = 0, 0, 0
        for item in count_list:
            if item['result'] == '异常':
                error_count = item['count']
            elif item['result'] == '成功':
                pass_count = item['count']
            elif item['result'] == '失败':
                fail_count = item['count']

        content = content.replace('$pass-count', str(pass_count))
        content = content.replace('$fail-count', str(fail_count))
        content = content.replace('$error-count', str(error_count))

        test_result = ''
        for result in result_list:
            test_result += '<tr height="40">'
            test_result += '<td width="7%%">%d</td>' % result['id']
            test_result += '<td width="9%%">%s</td>' % result['module']
            test_result += '<td width="9%%">%s</td>' % result['testtype']
            test_result += '<td width="7%%">%s</td>' % result['caseid']
            test_result += '<td width="20%%">%s</td>' % result['casetitle']

            if result['result'] == '成功':
                test_result += '<td width="7%%" bgcolor="lightgreen">%s</td>' % result['result']
            elif result['result'] == '失败':
                test_result += '<td width="7%%" bgcolor="red">%s</td>' % result['result']
            else:
                test_result += '<td width="7%%" bgcolor="blue">%s</td>' % result['result']

            test_result += '<td width="16%%">%s</td>' % result['testtime']
            test_result += '<td width="15%%">%s</td>' % result['error']
            if result['screenshot'] == '无':
                test_result += '<td width="10%%">%s</td>' % result['screenshot']
            else:
                test_result += '<td width="10%%"><a href="%s">%s</a></td>' % (result['screenshot'], result['screenshot'])
            test_result += '</tr>\n'

        content = content.replace('$test-result', str(test_result))

        report_name = './report/' + time.strftime('Report_%Y%m%d_%H%M%S.html')
        with open(report_name, mode='w+', encoding='utf-8') as file:
            file.write(content)


    def write_result(self, module, testtype, caseid, casetitle, result="成功", error="无", screenshot="无"):
        conn = pymysql.connect(user='root', passwd='123456', host='localhost', db='test', charset='utf8')
        cursor = conn.cursor()
        test_time = time.strftime("%Y-%m-%d %H:%M:%S")
        sql = "insert into report(version, module, testtype, caseid, " \
              "casetitle, result, testtime, error, screenshot) " \
              "values('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % \
              (self.version, module, testtype, caseid, casetitle, result, test_time, error, screenshot)
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()

        # 如果当前某个测试用例执行失败，则提交该测试用例到缺陷管理库中
        # 如果该缺陷已经提交了？是否存在重复提交的问题？
        if result == "失败" or result == "异常":
            self.submit_defect()

    def submit_defect(self):
        pass


    def capture_screenshot(self):
        file_name = "./report/" + time.strftime("%Y%m%d_%H%M%S") + ".png"
        ImageGrab.grab().save(file_name)
        return file_name


if __name__ == '__main__':
    report = HTMLReporter('1.1.3')
    report.generate_report()