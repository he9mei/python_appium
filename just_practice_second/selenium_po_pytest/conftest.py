from selenium import webdriver
import pytest
import time

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

    request.addfinalizer(end)

    return driver


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






