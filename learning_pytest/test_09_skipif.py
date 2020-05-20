'''
1.学习目标：掌握skipif的使用方法
2.语法
@pytest.mark.skipif(条件，原因)
  ---修饰在测试用例前
  ---条件为真时，执行跳过
注意：
@pytest.mark.skipif(2 > 1, reason="条件为真，跳过测试")
@pytest.mark.skipif(2 > 1, "条件为真，跳过测试")--->这样写会报错，必须写上reason参数名
'''

import pytest


class TestSkip:
    @pytest.mark.skipif(2 > 1, reason="条件为真，跳过测试")
    def test_01(self):
        print("条件为真，跳过测试")
        assert 1

    @pytest.mark.skipif(2 < 1, reason="条件为真，跳过测试")
    def test_02(self):
        print("条件为假，不会跳过测试")
        assert 1


'''
执行结果是：
learning_pytest/test_09_skipif.py::TestSkip::test_01 SKIPPED
learning_pytest/test_09_skipif.py::TestSkip::test_02 条件为假，不会跳过测试
PASSED

'''