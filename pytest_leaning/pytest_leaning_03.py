'''
三、pytest 运行模式
1.运行后生成测试报告htmlReport
（1）安装
-->pip3 install -U pytest-html
（2）运行
-->pytest --html=report.html
指定报告路径：
-->pytest --html=./report/report.html
独立运行：
上面方法生成的报告，css是独立的，分享报告的时候样式会丢失，
为了更好的分享发邮件展示报告，可以把css样式合并到html里
-->pytest --html=report.html --self-contained-html

问题：
1.安装出现ssl证书问题，解决办法，尝试信任---成功
-->python3 -m pip install pytest-html --trusted-host=pypi.python.org
--trusted-host=pypi.org --trusted-host=files.pythonhosted.org
2.运行之后找不到文件在哪里，尝试给出路径：
pytest --html=/Users/hehuaimei/PycharmProjects/python_appium/report.html


附加：
pytest-html参考：
https://www.cnblogs.com/yoyoketang/p/9444463.html

'''