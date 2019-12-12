'''
该实例练习order排序
0 0.1 0.2 1 不加修饰 -1 -0.2 -0.1
'''

import pytest

class TestCase:
    @pytest.mark.run(order=-1)
    def test_01(self):
        print("order=-1")

    @pytest.mark.run(order=1)
    def test_02(self):
        print("order=1")

    @pytest.mark.run(order=0.2)
    def test_03(self):
        print("order=0.2")

    @pytest.mark.run(order=0.1)
    def test_04(self):
        print("order=0.1")

    @pytest.mark.run(order=-0.1)
    def test_05(self):
        print("order=-0.1")

    @pytest.mark.run(order=-0.2)
    def test_06(self):
        print("order=-0.2")

    @pytest.mark.run(order=0)
    def test_07(self):
        print("order=0")

    def test_08(self):
        print("不加修饰")

'''
执行结果是：
order=0
.order=0.1
.order=0.2
.order=1
.不加修饰
.order=-1
.order=-0.2
.order=-0.1

'''

