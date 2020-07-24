from selenium import webdriver
import pytest
import time
import yagmail

'''
# 获取driver，打开浏览器，返回driver
@pytest.fixture(scope="session")
def get_driver():
    driver=webdriver.Chrome()
    driver.implicitly_wait(10)
    return driver

# yield方式无法返回值
@pytest.fixture(scope="session")
def open_yield():
    print("测试前执行")

    yield
    print("测试后执行")
'''


# addfinalizer方式，返回driver，且用例完成后关闭driver
@pytest.fixture(scope="session")
def open_addfinalizer(request):
    driver=webdriver.Chrome()
    print("获取driver")
    driver.implicitly_wait(10)

    def end():
        time.sleep(5)
        driver.quit()
        print("关闭driver")
        # send_mail("./report/report.html")  #发送html报告
        # 问题1：报告格式丢失
        # 解决：以下生成报告后能够保留格式
        # --html=./report/report.html --self-contained-html
        # 问题2：删掉已有的文件，执行后提示文件不存在，因为文件还没来得及生成
        # 尝试：增加等待时间；用绝对路径，都不行。执行完之后才生成报告。
        # 应该把发送报告单独拿出来，在全部执行完成之后才发送。
        # time.sleep(10)
        # send_mail("/Users/hehuaimei/PycharmProjects/python_appium/po_selenium_2/report/report.html")

    request.addfinalizer(end)

    return driver


def send_mail(attachment):
    yag=yagmail.SMTP(user="hehuaimei123@163.com",
                     password="8uhb*UHB",
                     host="smtp.163.com")
    subject="python测试报告"
    contents="selenium+po+pytest测试报告"
    yag.send(["hehuaimei123@163.com","hehuaimei@dangdang.com"],
             subject,
             contents,
             attachment)
    print("邮件已发送")


# fixture的参数化-单个参数
@pytest.fixture(scope="session",params=["18500000001","18500000002"])
def register(request):
    return request.param


# fixture的参数化-多个参数
@pytest.fixture(scope="session",params=[("18500000001","111111"),("1850000001","222222")])
def login(request):
    return request.param


# 无返回值的fixture
@pytest.fixture(scope="session")
def before():
    print("测试之前执行")








