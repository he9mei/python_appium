'''
from pytest付费课程

pytest插件补充：
1.pytest-html---测试报告（前面已练习）
补充：可以把 --html=./report/report.html 命令加到ini配置文件中
同理，也可以把allue命令 --alluredir="%allure_result_folder%" 加到ini配置文件中
打开allure报告的命令是 allure serve %allure_result_folder%  打开后ctrl+c退出命令

2.pytest-ordering 控制测试用例执行顺序
默认情况下，pytest是根据测试用例代码从上到下执行的，可以通过第三方插件改变顺序。
（1）安装：pip3 install pytest-ordering   （安装结果：在pycharm的Terminal安装，成功）
（2）使用方式：
标记与被测函数也就是测试用例：@pytest.mark.run(order=x);根据order传入的参数来确定顺序。
如果都是正数或者都是负数，值越小优先级越高；正数优先级高于负数。

见实例test_07.py
优先级是：0 0.1 0.2 1 不加修饰 -1 -0.2 -0.1
总结为：0>正数(值越小优先级越高)>不加修饰>负数(值越小优先级越高)

遇到问题：
安装pytest-ordering完成之后。
在被测用例前加上
@pytest.mark.run(order=x)时，@pyetest.mark下实际无法找到run标记，但是执行没有报错。

3.失败重跑--前面已介绍
安装：pip3 install pytest-rerunfailues
补充：使用时可以把命令 --reruns=2 加到pytest.ini文件中
练习见test_08.py

'''