'''
该实例练习类级别和方法级别的setup和teardown
注意：测试用例、main方法、setup/teardown函数都要写在类中

'''
import pytest


class TestCase:
    def test_01(self):
        print("test_01")
        assert 1

    def test_02(self):
        print("test_02")
        assert 1

    if __name__ == "__main__":
        pytest.main("-s test_06.py")

    def setup_class(self):
        print("setup_class在类之前执行")

    def teardown_class(self):
        print("teardown_class在类之后执行")

    def setup_method(self):
        print("setup_method在方法之前执行")

    def teardown_method(self):
        print("teardown_method在方法之后执行")

