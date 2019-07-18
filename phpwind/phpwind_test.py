# -*- coding: utf-8 -*-
import requests,time,re
from requests_toolbelt.multipart.encoder import MultipartEncoder

class phptest():
    def post_message(self):
        res = requests.post("http://localhost/phpwind/upload/login.php?",{'pwuser':'admin','pwpwd':'admin',
                                                                   'jumpurl':'http://localhost/phpwind/upload/',
                                                                   'step':'2','cktime':'31536000','hideid':'0',
                                                                   'lgt':'0'})
        print(res.text())
        time.sleep(2)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
            'Content-Type':''
        }
        multipart_encoder = MultipartEncoder(
            fields={
                'verify': (None, '44ff9c07'),
                'atc_title': (None, 'test09'),
                'atc_content': (None, 'test09'),
                'fid': (None, '4'),
                'action': (None, 'new'),
                'atc_credittype': (None, 'money'),
                'atc_enhidetype':(None,'rvrc'),
                'att_ctype1':(None,'money'),
            },
            boundary='----WebKitFormBoundaryF0Bmy436RHovZuOW'
        )
        # cookies='admin_basic=state; username=admin; password=admin; sessionid=z92gclarc29eiuyalpql48ua6jtmx6sr; 98edd_ol_offset=97; 98edd_ipstate=1550913421; 98edd_threadlog=%2C6%2C8%2C; 98edd_lastpos=index; 98edd_lastvisit=2173%091550998071%09%2Fphpwind%2Findex.php%3F; 4cfdf_ol_offset=97; 4cfdf_ipstate=1550998566; 4cfdf_AdminUser=BVYNCVVWAwIPAGpUBg5bWGoHB1MPCV1QV1NWClRUBgADAVJSUlJaWlBXBwBVCQZQVGo%3D; 4cfdf_readlog=%2C1%2C2%2C3%2C4%2C5%2C6%2C7%2C8%2C9%2C10%2C; 4cfdf_ck_info=%2F%09; 4cfdf_winduser=BWoAC1dWUVZRCFJUWgcLDgYBUQUIDlxQCgZWCgENUwEGUGo%3D; 4cfdf_threadlog=%2C2%2C3%2C4%2C; 4cfdf_lastpos=other; 4cfdf_lastvisit=228%091551016814%09%2Fphpwind%2Fupload%2Fpost.php%3Ffid%3D4'
        # cookies={'admin_basic':'state',' username':'admin',' password':'admin',' sessionid':'z92gclarc29eiuyalpql48ua6jtmx6sr',' 98edd_ol_offset':'97',' 98edd_ipstate':'1550913421',' 98edd_threadlog':'%2C6%2C8%2C',' 98edd_lastpos':'index',' 98edd_lastvisit':'2173%091550998071%09%2Fphpwind%2Findex.php%3F',' 4cfdf_ol_offset':'97',' 4cfdf_ipstate':'1550998566',' 4cfdf_AdminUser':'BVYNCVVWAwIPAGpUBg5bWGoHB1MPCV1QV1NWClRUBgADAVJSUlJaWlBXBwBVCQZQVGo%3D',' 4cfdf_readlog':'%2C1%2C2%2C3%2C4%2C5%2C6%2C7%2C8%2C9%2C10%2C',' 4cfdf_ck_info':'%2F%09',' 4cfdf_winduser':'BWoAC1dWUVZRCFJUWgcLDgYBUQUIDlxQCgZWCgENUwEGUGo%3D',' 4cfdf_threadlog':'%2C2%2C3%2C4%2C',' 4cfdf_lastpos':'other',' 4cfdf_lastvisit':'228%091551016814%09%2Fphpwind%2Fupload%2Fpost.php%3Ffid%3D4'}
        headers['Content-Type'] = multipart_encoder.content_type
        re = requests.post('http://localhost/phpwind/upload/post.php?',data=multipart_encoder, headers=headers,cookies=res.cookies)
        # payload = """------WebKitFormBoundaryF0Bmy436RHovZuOW\r\nContent-Disposition: form-data;
        #     name=\"verify\"\n\n{}\r\n------WebKitFormBoundaryF0Bmy436RHovZuOW\r\nContent-Disposition: form-data;
        #     name=\"atc_title\"\n\n{}\r\n------WebKitFormBoundaryF0Bmy436RHovZuOW\r\nContent-Disposition: form-data;
        #     name=\"atc_content\"\r\n\r\n{}\r\n------WebKitFormBoundaryF0Bmy436RHovZuOW\r\nContent-Disposition: form-data;
        #     name=\"fid\"\r\n\r\n {}\r\n----WebKitFormBoundaryF0Bmy436RHovZuOW--""".format('44ff9c07', 'test09','test09',
        #                                                                                    '1',
        #                                                                                         [201, ])
        # headers = {
        #     "content-type": "multipart/form-data; boundary=------WebKitFormBoundaryF0Bmy436RHovZuOW"
        # }
        # resp = requests.post('http://localhost/phpwind/upload/post.php?', data=payload,
        #                      verify=False, timeout=10, headers=headers,cookies=res.cookies)
        # print(resp.request.body)


if __name__ == '__main__':
    phptest().post_message()