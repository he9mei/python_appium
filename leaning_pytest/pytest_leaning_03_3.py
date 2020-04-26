'''
三、pytest 运行模式---插件
2.运行指定的case---02.py已总结
3.多进程运行cases
当cases量很多时，运行时间也会变的很长，如果想缩短脚本运行的时长，就可以用多进程来运行。其中NUM填写并发的进程数。
（1）安装
-->pip install -U pytest-xdist
（2）运行
-->pytest test_se.py -n NUM
实际操作结果：
在pycharm的Terminal安装成功。
执行-->pytest -n 2   #运行成功

4.重试运行cases
在做接口测试时，有事会遇到503或短时的网络波动，导致case运行失败，
而这并非是我们期望的结果，此时可以就可以通过重试运行cases的方式来解决。
（1）安装
-->pip install -U pytest-rerunfailures
（2）运行
-->pytest test_se.py --reruns NUM
实际操作结果：
在pycharm的Terminal安装成功。
执行-->pytest --reruns 3   #运行成功
执行--> pytest leaning_pytest/test_03.py::TestDemo::test_fun_3 --reruns 3  #运行成功

5.显示print内容---02.py已总结

参考：
https://www.jianshu.com/p/932a4d9f78f8


'''
