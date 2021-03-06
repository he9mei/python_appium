'''
使用装饰器引用fixture
----fixture标记的函数可以应用于类的外部
@pytest.fixture()
def fixture名（）：
    代码块
@pytest.mark.usefixtures("fixture名")
class 类：
    def 函数(self)：
        测试用例
'''

import pytest
@pytest.fixture(scope="module")
def before():
    print("---before---")

# @pytest.mark.usefixtures("before")
class TestFixture:
    def test_1(self):
        print("测试用例1")

    @pytest.mark.usefixtures("before")
    def test_2(self):
        print("测试用例2")

if __name__=="__main__":
    pytest.main(["-s","-v","test_12_fixture_5.py"])