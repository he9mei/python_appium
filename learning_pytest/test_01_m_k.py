# 涉及知识点：
# 用例的写法
# 配合验证用例的执行

import pytest

class TestDemo:
    @pytest.mark.testicon  #可以用，但是会提示警告。因为testicon是自己随便写的标签，不是官方的标签。
    def test_test1(self):
        print("测试用例1-测试用例1")

    def test_login_test2(self):
        print("测试用例1-测试用例2")

    if __name__=="__main__":
        # pytest.main(["-s","-v","./test_01_m_k.py","-m","testicon"]) # test1用testicon标记，使用时：-m "testicon"
        pytest.main(["-s", "-v", "./test_01_m_k.py", "-k", "login"]) # test2有关键字login，使用时：-k "login"

