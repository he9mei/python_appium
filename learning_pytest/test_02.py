# 涉及知识点：
# 配合验证用例的执行
import pytest

@pytest.mark.skip
class TestDemo:
    def test_test1(self):
        print("测试用例2-测试用例1")
    def test_test2(self):
        print("测试用例2-测试用例2")