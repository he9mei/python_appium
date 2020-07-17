from time import sleep
import pytest

def test_01():
    sleep(5)

def test_02():
    sleep(3)

def test_03():
    sleep(1)

if __name__=="__main__":
    # pytest.main(["-s","-v","test_13_xdist.py"])
    # pytest.main(["-s", "-v", "test_13_xdist.py","-n","2"])  # 无法识别unrecognized arguments: -n 2
    pytest.main(["-s", "-v", "test_13_xdist.py","--tests-per-worker","auto"])



'''
普通执行
-->python ./test_13_xdist.py
 3 passed in 9.03s 
 
 pytest-xdist多进程执行
 -->python ./test_13_xdist.py -n 2
 报错： unrecognized arguments: -n 2
 
 -->python ./test_13_xdist.py --tests-per-worker auto
 3 passed in 5.11s 
'''