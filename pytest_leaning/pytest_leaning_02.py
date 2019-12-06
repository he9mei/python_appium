'''
二、用例执行
1.在pycharm的Terminal执行用例：
默认路径即当前项目，如rootdir: /Users/hehuaimei/PycharmProjects/python_appium
（也可以在cmd执行，先cd进入项目目录）

-->pytest
当前路径下的用例全部执行
pytest_leaning/test_01.py ..                                                                                                       [ 50%]
pytest_leaning/test_02.py ..

-->pyetst -s -m "test"
针对标记执行某些用例
配合使用的是在函数前加上@pytest.mark.test
后面这个test是随便取得名字，识别不了，会报警。
mark标记官方文档：https://docs.pytest.org/en/latest/mark.html
报警解决办法：https://www.cnblogs.com/TestTan/p/11493177.html

-->pytest pytest_leaning/test_01.py
执行指定路径/指定py文件
如果不想执行某些类或者函数，可标记跳过，在该类或函数前加上：@pytest.mark.skip

-->pytest pytest_leaning/test_01.py::TestDemo
执行指定路径/指定py文件::指定class

-->pytest pytest_leaning/test_01.py::TestDemo::test_test1
执行指定路径/指定py文件::指定class::指定函数

2.常用参数说明：
-v：说明：可以输出用例更加详细的执行信息，比如用例所在的文件及用例名称等
-s：说明：输入我们用例中的调式信息，比如print的打印信息等
-m ：说明：执行特定的测试用例,”标记“
-k： 说明：执行用例包含“关键字”的用例 ,"关键字"
-q： 说明：简化控制台的输出
--lf：当一次用例执行完成后，如果其中存在失败的测试用例，那么我们可以使用此命令重新运行失败的测试用例
--ff：如果上次测试用例出现失败的用例，当使用--ff后，失败的测试用例会首先执行，剩余的用例也会再次执行一次
进一步说明：
-v
加上-v可以看到每个函数的执行结果。如，
pytest -v pytest_leaning/test_01.py
结果为：
pytest_leaning/test_01.py::TestDemo::test_test1 PASSED                                                                             [ 50%]
pytest_leaning/test_01.py::TestDemo::test_test2 PASSED
其他的，如关键字k，失败重跑lf、ff后续再验证。
-m
如果用例中包含多个分组，想要只运行其中一个组，则使用-m "组名"的方式。
使用方式是，再函数前加上@pytest.mark.test (test是自己定义的名字，报警解决办法见前面的链接)
执行时，使用-->pytest -m "test"
-k
k选项允许我们设置表达式来运行某些用例,表达式的写法有许多，
可以用全称如test_case1这样也可以去掉test_，除了or外也可以使用not来指定那些用例不跑；
执行时，使用-->pytest -v -k "test_01 or test_02" 即执行test_01和test_02两个py文件
执行时，使用--> pytest -v -k "not test_02" 即除了test_02这个py文件不执行，其他都执行
-x
pytest的原本运行规则是每条用例均执行，不管是否有失败，如果我们想在用例运行时遇到失败即停止，则可以使用-x

pytest其他用法，如
-->pytest --help
-->pytest --version

3.执行结果
绿色..表示成功；s表示跳过；F表示失败

附加：
关于pytest用例执行文档：
https://www.cnblogs.com/test000/p/11613459.html
https://blog.csdn.net/df0128/article/details/91043150


'''

