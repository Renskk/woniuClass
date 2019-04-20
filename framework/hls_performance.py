import urllib3, time, os, random, threading, requests

# 忽略HTTPS证书警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
urllib3.disable_warnings(urllib3.exceptions.SubjectAltNameWarning)

class HLSPerformance:
    def __init__(self):
        pass

    # 定义解析M3U8文件的方法，并将ts文件名返回到一个列表中
    def read_m3u8(self, path):
        temp_list = []
        with open(path) as file:
            temp_list = file.readlines()

        ts_list = []
        for line in temp_list:
            if line.strip().endswith(".ts"):
                ts_list.append(line.strip())

        return ts_list

    # 将ts文件进行下载，并统计每一次下载的响应时间
    def download_ts(self):
        url_prefix = 'https://dco4urblvsasc.cloudfront.net/811/81095_ywfZjAuP/game/'
        path = r'C:\Users\Denny\Downloads\500kbps(1).m3u8'
        ts_list = self.read_m3u8(path)
        for i in range(5):
            start_time = int(time.time()*1000)
            resp = requests.get(url_prefix + ts_list[i], verify=False)
            with open('D:/%s' % ts_list[i], mode='wb+') as file:
                file.write(resp.content)
            end_time = int(time.time() * 1000)
            print("响应时间为：%d" % (end_time-start_time))

        # 显示线程名称，可根据线程名称创建文件，将每一个切片文件下载到对应的目录下。
        print(threading.current_thread().getName())


if __name__ == '__main__':
    hls = HLSPerformance()
    # hls.download_ts()
    for i in range(1):
        threading.Thread(target=hls.download_ts).start()