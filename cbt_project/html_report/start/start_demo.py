# -*- coding: utf-8 -*-
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
#禅道提交BUG
class ExecuteScript:
    def __init__(self):
        pass
    def test_demo(self):
        se = requests.session()
        res =se.post('http://192.168.2.181/zentaopms/www/index.php?m=user&f=login',{'account':'leitao','password':'123'})
        headers = {'Content-Type':''}
        multipart_encoder = MultipartEncoder(
            fields={
                'product': (None, '2'),
                'module': (None, '4'),
                'project': (None, '3'),
                'openedBuild[]': (None, '1'),
                'assignedTo': (None, 'leitao'),
                'type': (None, 'codeerror'),
                'os':(None,'all'),
                'browser':(None,'all'),
                'title':(None,'这里有个BUG'),
                'severity':(None,'3'),
                'case':(None,'0'),
                'caseVersion':(None,'0'),
                'result':(None,'0'),
                'testtask':(None,'0')
            },
            boundary='----WebKitFormBoundaryOci1m9tnAwxBhnWZ'
        )
        headers['Content-Type'] = multipart_encoder.content_type
        re = se.post('http://192.168.2.181/zentaopms/www/index.php?m=bug&f=create&productID=2&branch=0&extra=moduleID=0',
                           headers = headers,data=multipart_encoder)

if __name__ == '__main__':
    ExecuteScript().test_demo()