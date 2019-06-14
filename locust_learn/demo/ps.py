import psutil,time,locust

def monitor(seconds):
    print('cpu---memory---disk---process---')
    while(True):
        cpu = psutil.cpu_percent()
        memory =psutil.virtual_memory()
        dick = psutil.disk_usage("c:")
        process = psutil.pids()
        res = (str(cpu)+'%   '+str(memory.percent)+'%   '+str(dick.percent)+'%   '+str(len(process)))
        print(res)
        time.sleep(seconds)

monitor(2)


##################内存资源
# per = psutil.virtual_memory().percent#虚拟内存消耗
# print(str(per)+'%')
# print(psutil.virtual_memory().available)#可用资源
# print(psutil.virtual_memory().total)#总计
# print(psutil.virtual_memory().used)#已用资源
# print(psutil.virtual_memory().free)#空闲资源

#################进程ID
# print(psutil.pids())
# print(len(psutil.pids()))#进程的ID数

################硬盘信息
# print(psutil.disk_partitions())#硬盘的详细信息

################网络IO
# print(psutil.net_io_counters())#网络的IO数据统计
# print(psutil.net_io_counters().bytes_recv)#受到数据包的数量
# print(psutil.net_io_counters().bytes_sent)#发送的字节数
# print(psutil.net_io_counters().dropin)#收到的丢包数

################cpu消耗数据统计
# print(psutil.cpu_percent())#cpu利用率

################磁盘信息统计
# print(psutil.disk_usage('e:'))#e盘的消耗数据
# print(psutil.disk_usage('c:').free)#c盘的空闲
# print(psutil.disk_usage('c:').percent)#c盘的利用率

################统计本地人任务管理器的进程消耗
# print(psutil.test())


