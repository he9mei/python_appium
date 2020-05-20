import unittest
from learning_unittest.HTMLTestRunner import HTMLTestRunner
import os
import time
import yagmail


def send_mail(attachment):
    yag=yagmail.SMTP(user="hehuaimei123@163.com",
                 password="8uhb*UHB",
                 host="smtp.163.com")
    subject="自动化测试报告"
    contents="python自动化测试报告，自动发送。"
    yag.send(["hehuaimei@dangdang.com","hehuaimei123@163.com"],subject,contents,attachment)
    print("自动化测试报告已发送！")


if __name__=="__main__":

    #定义要执行的测试套件suit
    top_level_dir = "/Users/hehuaimei/PycharmProjects/python_appium/learning_unittest"
    start_dir = "./test_case"
    # pattern="test_*.py"  #执行"test_"开头的用例
    pattern = "test_baidu_search_ddt_data.py"  # 方便测试，暂时只执行一个文件

    suit = unittest.defaultTestLoader.discover(start_dir, pattern, top_level_dir)

    #定义测试runner
    now_time=time.strftime("%Y_%m_%d_%H_%M_%S",time.localtime(time.time()))  #时间
    path="./report"
    if not os.path.exists(path):
        os.makedirs(path)
    html_report=path + "/"+now_time+"_report.html"
    fp = open(html_report, "wb")  #报告标题加上时间
    runner=HTMLTestRunner(stream=fp,title="我的测试报告",description="运行环境：mac")

    #执行用例，执行完毕后关闭报告文件，发送邮件
    runner.run(suit,rerun=1, save_last_run=True)
    fp.close()
    send_mail(html_report)


# 结果：
# 生成报告成功，且可以实现自动重跑
# 发送报告成功