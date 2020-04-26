# 涉及知识点：
# case执行失败 会显示详细的失败信息
# 断言assert---待学习
# 不太明白 assert hasattr(s,"check")

import pytest

@pytest.mark.skip
class TestDemo:
    def func(self,x):
        return x+1
    @pytest.mark.skip
    def test_func_1(self):
        assert self.func(3)==5

    @pytest.mark.skip
    def test_func_2(self):
        s="hell"
        assert "h" in s
    def test_fun_3(self):
        s="hello"
        assert hasattr(s,"check")


