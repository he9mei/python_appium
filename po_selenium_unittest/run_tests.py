
import unittest
from po_selenium_unittest.test_case.test_01_search import TestSearch
from po_selenium_unittest.HTMLTestRunner import HTMLTestRunner
import time
import os

if __name__ == "__main__":
    # 配置suite和runner最基本的用法
    # suite = unittest.TestSuite()
    # suite.addTest(TestSearch("test_1_search"))    # 需要导入相应的class，否则会报错
    # suite.addTest(TestSearch("test_2_search"))
    #
    # runner = unittest.TextTestRunner()

    #  配置suite和runner进阶用法
    start_dir = "./test_case"
    # pattern = "test*.py"
    pattern = "test_01_search.py"
    suite = unittest.defaultTestLoader.discover(start_dir, pattern)

    now = time.strftime("%Y-%m-%d_%H-%M-%S")
    path = "./report"
    if not os.path.exists(path):
        os.makedirs(path)
    html_report = path+"/"+now+"_report.html"
    fp = open(html_report, "wb")
    runner = HTMLTestRunner(stream=fp, title="自动化测试报告", description="运行环境：Windows")
    # with open(html_report, "wb") as fp:  # 这样写不行，会报错，区别是什么？

    # 执行
    runner.run(suite, rerun=1, save_last_run=True)
    fp.close()
