'''
一、理论知识：

1.pytest是一个非常成熟的全功能的Python测试框架，主要有以下几个特点：

简单灵活，容易上手
支持参数化
能够支持简单的单元测试和复杂的功能测试，还可以用来做selenium/appnium等自动化测试、接口自动化测试（pytest+requests）
pytest具有很多第三方插件，并且可以自定义扩展，比较好用的如pytest-selenium（集成selenium）、pytest-html（完美html测试报告生成）、
pytest-rerunfailures（失败case重复执行）、pytest-xdist（多CPU分发）等
测试用例的skip和xfail处理
可以很好的和jenkins集成
report框架----allure 也支持了pytest

2.如何编写pytest测试样例

编写pytest测试样例非常简单，只需要按照下面的规则：
测试文件以test_开头（以_test结尾也可以）
测试类以Test开头，并且不能带有 init 方法
测试函数以test_开头
断言使用基本的assert即可

附加：
关于pytest测试框架文档：
https://www.jianshu.com/p/932a4d9f78f8

3.pytest安装
在终端安装
-->pip3 install -U pytest
或者直接在pycharm使用pytest时也会提示并引导安装

'''


