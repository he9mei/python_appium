import unittest
from leaning_unittest.HTMLTestRunner import HTMLTestRunner
import os
import time

top_level_dir="/Users/hehuaimei/PycharmProjects/python_appium/leaning_unittest"
start_dir="./test_case"
pattern="test*.py"

suit=unittest.defaultTestLoader.discover(start_dir,pattern,top_level_dir)

if __name__=="__main__":
    # runner=unittest.TextTestRunner()
    now_time=time.strftime("%Y_%m_%d_%H_%M_%S",time.localtime(time.time()))  #时间
    path="./report"
    if not os.path.exists(path):
        os.makedirs(path)
    # fp = open(path+"/report.html", "wb")
    fp = open(path + "/"+now_time+"_report.html", "wb")  #报告标题加上时间
    runner=HTMLTestRunner(stream=fp,title="我的测试报告",description="运行环境：mac")
    runner.run(suit,rerun=1, save_last_run=True)
    fp.close()


# 结果：
# 生成报告成功，且可以实现自动重跑