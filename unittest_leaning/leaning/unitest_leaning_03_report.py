'''
一、测试报告
1.克隆以下项目，
（1）把HTMLTestRunner.py单独放到python安装目录下，如c:\python37\lib\
（终端进入python，输入import HTMLTestRunner验证是否成功）
（2）还有一种方法是把HTMLTestRunner.py放到项目目录中。
GitHub地址：https://github.com/defnngj/HTMLTestRunner
克隆方法：VCS-->checkout from version control-->git 填写以上地址和存储位置即可。

2.生成html测试报告
（1）在HTMLTestRunner.py找到class HTMLTestRunner查看源代码
（2）修改run_tests.py文件---见run_tests_has_report.py

3.更易读的测试报告
python注释分为两种，一种是comment，另一种是docstring；前者是普通注释，后者用于描述函数、类和方法。
用一对三引号表示。这类注释平时调用不会显示，只有通过help()方法查看才会显示。
HTMLTestRunner可以读取doc string类型的注释，所以我们在测试用例中添加这类注释，即可在报告中显示。

4.测试报告的文件名
文件名加上时间。
now_time=time.strftime("%Y_%m_%d_%H_%M_%S",time.localtime(time.time()))  #时间

'''