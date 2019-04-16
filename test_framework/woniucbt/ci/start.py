from test_framework_43.woniucbt.ci.ci import CI
import time

# 定时任务，在相同的间隔时间内完成持续集成：
# while True:
    # ci = CI('1.1.6')
    # ci.svn()
    # ci.ant()
    # ci.deploy()
    # ci.start()
    # ci.test()
    # ci.email()
    #
    # time.sleep(6000)


# 定时任务：daily build，每日构建
# while True:
#     hour = time.strftime('%H')
#     minute = time.strftime('%m')
#
#     if hour == '2' and minute == '30':
#         ci = CI('1.1.6')
#         ci.svn()
#         ci.ant()
#         ci.deploy()
#         ci.start()
#         ci.test()
#         ci.email()
#
#         time.sleep(30)



# 当有代码提交时，则进行持续集成（如何知道程序员提交了代码呢？）
