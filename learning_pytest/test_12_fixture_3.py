'''
2.yield和addfinalizerq的区别
(1)yield：当用例执行完毕之后，会执行yield后面的代码，但不能return
(2)addfinalizer这个实现功能与yield一样，可以return参数，传给后面的用例
'''

#实例2

import pytest
from selenium import webdriver

#创建fixture
@pytest.fixture(scope="session",autouse=True)
def open(request):
    driver=webdriver.Chrome()
    print("打开浏览器")

    def end():
        driver.quit()
        print("关闭浏览器")

    request.addfinalizer(end)  #终结函数，作用与yield一样
    return driver

#使用fixture
def test_baidu(open):
    open.get("http://www.baidu.com")
    title=open.title
    print(f"百度首页标题是：{title}")
    assert "百度" in title

if __name__=="__main__":
    pytest.main(["-s","-v","test_12_fixture_3.py"])

'''
执行结果：
打开浏览器
百度首页标题是：百度一下，你就知道
'''