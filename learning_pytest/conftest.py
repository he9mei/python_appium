
import pytest
from selenium import webdriver
from time import sleep


@pytest.fixture(scope="session")
# @pytest.fixture(scope="session",autouse=True)
# #如果需要返回值，还是需要使用参数传入的形式，autouse也拿不到返回值。
def driver(request):
    driver=webdriver.Chrome()
    driver.implicitly_wait(10)
    print("启动driver")

    def end():
        sleep(5)
        driver.quit()
        print("关闭driver")

    request.addfinalizer(end)

    return driver


# 补充：使用钩子函数传值
@pytest.fixture(scope="session",autouse=True)
def url():
    return "http://www.baidu.com"