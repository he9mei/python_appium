'''
验证py文件内执行，__main__方法
测试用例可以写在类中，也可以不需要类直接写在函数中
'''
import pytest

# @pytest.mark.skip
def test_01():
    print("test_01")
    assert 1

def test_02():
    print("test_02")
    assert 0

#执行方式：
#1.直接在pycharm的当前py文件使用右键即ide执行，不需要main函数，写了也不会使用main里面的参数。py文件内全部执行，也没有带参数。
#2.py文件内写main函数，在pytest.main()中写入执行参数。执行时，在terminal执行：先到当前路径
# ---> python ./test_04_main.py

if __name__=="__main__":
    # pytest.main("-s test_04_main.py")  # 这种写法，在terminal执行时会报错，参数需要写成list形式
    pytest.main(["-s","-v","./test_04_main.py::test_02","--reruns","2"])