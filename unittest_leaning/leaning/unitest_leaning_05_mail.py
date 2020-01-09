'''
三、自动发送邮件
1.用python自带的发送邮件功能
2.更简单的发送邮件的方式：
(1)yagmail的安装
yagmail是Python的一个第三方库，可以让我们以非常简单的方法实现自动发送邮件功能。
GitHub项目地址：https：//github.com/kootenpv/yagmail。
通过pip命令安装。
pip install yagmail
实际操作：
pip3 install yagmail --trusted-host=pypi.python.org --trusted-host=pypi.org --trusted-host=files.pythonhosted.org
结果：安装成功啦！

(2)yagmail的使用
见send_yagmail.py

(3)测试用例执行完毕之后，实现自动发送报告
a.与unittest结合实现
见run_tests_has_report_email.py
b.与pytest结合实现

'''