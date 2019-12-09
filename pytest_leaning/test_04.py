'''
验证py文件内执行，__main__方法
测试用例可以写在类中，也可以不需要类直接写在函数中
'''
import pytest
@pytest.mark.skip
def test_01():
    print("test_01")
    assert 1
def test_02():
    print("test_02")
    assert 0
if __name__=="__main__":
    pytest.main("-s test_04.py")
