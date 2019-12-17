'''
1、学习目标：必须掌握fixture的创建和使用
2、语法：
（1）创建一个fixture
@pytest.fixture()
def fixture名()：
    代码块
（2）使用fixture
def 测试用例(fixture名)：
    用例步骤
3、编写一个fixture,并且用在测试用例中
'''

import pytest

#创建fixture
@pytest.fixture()
def login():
    print("登录")

#使用fixture---将fixture当作参数使用
def test_shopping(login):
    print("测试购物，需要先登录")

def test_view():
    print("测试浏览商品，不需要登录")



