'''
该实例练习模块级别和函数级别的setup和teardwon
'''

import pytest

def test_01():
    print("test_01")
    assert 1

def test_02():
    print("test_02")
    assert 1

def setup_module():
    print("setup_module在.py文件之前执行")
def teardown_module():
    print("teardown_module在.py文件之后执行")

def setup_function():
    print("setup_function在函数之前执行")
def teardown_function():
    print("teardown_function在函数之后执行")

def setup():
    print("setup在函数/方法前执行")
def teardown():
    print("teardown在函数/方法前执行")

if __name__=="__main__":
    pytest.main(["-s","test_05_setup.py"])

# 执行：
#-->python ./test_05_setup.py

