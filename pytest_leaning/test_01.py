# 涉及知识点：
# 用例的写法
# 配合验证用例的执行

import pytest
@pytest.mark.skip
class TestDemo:
    # @pytest.mark.test  可以用，但是会提示警告。因为test是自己随便写的标签，不是官方的标签。
    # @pytest.mark.skip
    def test_test1(self):
        print("测试用例1-测试用例1")
    def test_test2(self):
        print("测试用例1-测试用例2")