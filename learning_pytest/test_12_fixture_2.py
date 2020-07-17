'''
二、fixture实现setup和teardown
1.结合yield---实现setup和teardown
(1)yield后面代码是用例执行完成后再执行的,相当于teardown
(2)如果其中一个用例遇到异常，不影响yield后面的teardown执行，运行结果互不影响，
并且全部用例执行完之后，yield呼唤teardown擦操作。

'''
import pytest
from selenium import webdriver

#实例1
#创建fixture
@pytest.fixture()
def open():
    print("打开浏览器")

    yield  #yield后面代码是用例执行完成后再执行的，相当于teardown
    print("关闭浏览器")
#使用fixture
def test_shoppping(open):
    print("测试购物")


# -----以下新增实际使用时的获取driver的setup和teardown------
# yield写法1---第1中写法的问题是，不能返回值
@pytest.fixture(scope="session",autouse=True)
def browser():
    driver=webdriver.Chrome()
    driver.implicitly_wait(10)
    print('启动driver')

    yield
    driver.quit()
    print("关闭driver")


# yield写法2---第2种写法，可以获得返回值
driver=None
@pytest.fixture(scope="session",autouse=True)
def browser():
    global driver
    driver=webdriver.Chrome()
    driver.implicitly_wait(10)
    print('启动driver')
    return driver

def browser_end():
    yield driver
    driver.quit()
    print("关闭driver")

# 第3种写法使用addfinalizer---第3种写法，可以获得返回值
@pytest.fixture(scope="session",autouse=True)
def browser(request):
    driver=webdriver.Chrome()
    driver.implicitly_wait(10)
    print("启动driver")

    def end():
        driver.quit()
        print("关闭driver")

    request.addfinalizer(end)
    return driver
