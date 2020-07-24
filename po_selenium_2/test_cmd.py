
import sys, os
sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))
# 以上是为了加入项目路径，解决pycharm可以执行，但是cmd无法执行的问题---未证实是否可行

def test_cmd():
    print("just test cmd")

#测试1-当成普通函数，直接调用函数，然后在cmd执行该文件
# test_cmd()
#-->python test_cmd.py

#测试2-写成测试用例，用pytest执行
#-->pytest -s -v test_cmd.py

