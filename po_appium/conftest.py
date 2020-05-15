
import pytest
from appium import webdriver
from time import sleep
import logging
import logging.config
import yagmail


caps = {
    # "automationName": "Appium",
    "automationName": "UIAutomator2",
    "platformName": "Android",
    # "platformVersion": "8.0.0",  #华为手机
    # "deviceName": "HMKNW17727007061",
    "platformVersion": "7.1.1",  #OPPO手机
    "deviceName": "MJA68TGES4S4SKAY",
    # "platformVersion": "5.1",  #乐蒙手机
    # "deviceName": "MUGW8SOWWEY75NNDM",
    "appPackage": "com.dangdang.reader",  #adb shell pm list package -3
    "appActivity": ".activity.GuideActivity",  #adb shell dumpsys activity |grep com.dangdang.reader |grep LAUNCHER
    "noReset": True
}


@pytest.fixture(scope="session")
def driver(request):
    driver = webdriver.Remote("http://localhost:4723/wd/hub",caps)
    driver.implicitly_wait(10)
    print("启动driver")

    def end():
        sleep(5)
        driver.quit()
        print("关闭driver")

    request.addfinalizer(end)
    return driver


'''
#也可以写成这种格式，先定义一个字典，再加数据
caps = {}
caps["automationName"] = "Appium"
caps["platformName"] = "Android"
caps["platformVersion"] = "8.0.0"
caps["deviceName"] = "HMKNW17727007061"
caps["appPackage"] = "com.dangdang.reader"
caps["appActivity"] = ".activity.GuideActivity"
caps["noReset"] = "true"   #"true"或者True都可以，但是如果不写这个，每次启动都会清缓存重新启动
'''

'''
@pytest.fixture(scope="session")
def logger():
    CONF_LOG = "./log_notUseNow.conf"
    logging.config.fileConfig(CONF_LOG)
    logger = logging.getLogger()
    print("---打印日志---")
    return logger

# 目前用到使用fixture传入logger的位置包括：
# (1)basic的init方法,传入logger；
# (2)继承basic的page类，实例化时，传入logger;
# (3)每一个测试用例方法,传入logger
# 
# 问题：log使用配置文件的形式，可以；但是无法根据功能做区分。
# 解决办法：
# 不使用fixture的方式调用；
# (conftest.py文件中logger注释；log.conf文件暂时改名，否则还是可以识别，不使用的话会报错)
# 封装方法获得logger，然后每个py文件调用该方法，并传入py_name
'''

#发送邮件，尝试在测试用例执行完毕之后，把测试报告当作附件发送
def send_mail(attachment):
    yag=yagmail.SMTP(user="hehuaimei123@163.com",
                 password="8uhb*UHB",
                 host="smtp.163.com")
    subject="自动化测试报告"
    contents="python自动化测试报告，自动发送。"
    yag.send(["hehuaimei@dangdang.com","hehuaimei123@163.com"],subject,contents,attachment)
    print("自动化测试报告已发送！")
'''
    # 执行完毕后自动发送邮件
    # send_mail("../test_result/report/html_report/report.html")
    # 问题1：report.html能正常发送，但是会丢失格式
    # 解决办法：--html=report.html --self-contained-html
    # send_mail("../test_result/report/allure_report")
    #问题2：发送文件夹会报错 TypeError: '../test_result/report/allure_report' is not a valid filepath
    # 用例执行完毕之前，报告还没有生成；这个时候发送，会找不到文件。
    # 并且allue-report不能直接打开，不能以文件夹形式发送
    #解决办法：使用jerkins执行用例，并且配置邮件自动发送allure和html两种报告
'''
