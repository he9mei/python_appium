# 涉及知识点：
# case执行失败 会显示详细的失败信息
# 断言assert:
# hasattr(object,name) 判断对象是否包含对应的属性，object是对象，name是属性名

import pytest


# @pytest.mark.skip
class TestDemo:

    def func(self,x):
        return x+1

    def func_2(self,a,b):
        return a>b

    # @pytest.mark.skip
    def test_1(self):
        # assert self.func(3)==5
        # assert self.func(3) != 5
        # assert 2>=1
        assert 2<=2

    # @pytest.mark.skip
    def test_2(self):
        s="hello"
        # assert "h" in s
        assert "k" not in s

    def test_3(self):
        s="hello"
        assert hasattr(s,"lower")  #s是字符串，有切换大小写的属性

    def test_4(self):
        # assert 1
        # assert 0
        assert True
        # assert not True
        # assert False

    def test_05(self):
        # assert self.func_2(2,1)
        # assert self.func_2(1,2)
        # assert self.func_2(2, 1) is True
        # assert self.func_2(2, 1) is not True
        assert self.func_2(2, 1) is False


if __name__ == "__main__":
    pytest.main(["-s","-v","test_03_assert.py"])


