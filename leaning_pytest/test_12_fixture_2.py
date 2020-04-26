'''
二、fixture实现setup和teardown
1.结合yield---实现setup和teardown
(1)yield后面代码是用例执行完成后再执行的,相当于teardown
(2)如果其中一个用例遇到异常，不影响yield后面的teardown执行，运行结果互不影响，
并且全部用例执行完之后，yield呼唤teardown擦操作。

'''
#实例1

import pytest
#创建fixture
@pytest.fixture()
def open():
    print("打开浏览器")

    yield  #yield后面代码是用例执行完成后再执行的，相当于teardown
    print("关闭浏览器")
#使用fixture
def test_shoppping(open):
    print("测试购物")
