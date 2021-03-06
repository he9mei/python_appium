'''
三、pytest 运行模式---插件
1.运行后生成测试报告-1

pytest-html报告模式
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
1.安装出现ssl证书问题，解决办法，尝试信任---成功解决
-->python3 -m pip install pytest-html --trusted-host=pypi.python.org
--trusted-host=pypi.org --trusted-host=files.pythonhosted.org
2.运行之后没有生成报告文件，pycharm的Terminal根本无法识别pytest --html
在pycharm的Terminal又按照以上命令重新安装了一次。---成功解决
执行命令：
-->pytest --html=./report/report.html  #自己指定路径
-->pytest --html=report.html --self-contained-html   #默认为当前项目路径;
备注：
--self-contained-html的作用是为了解决发送html报告附件导致报告格式丢失的问题。


附加：
pytest-html参考：
https://www.cnblogs.com/yoyoketang/p/9444463.html

书籍补充：
pytest无需安装插件的报告：
1.xml报告
pytest ./test.py --junit-xml=./report/junit-xml.xml
2.session-log链接
pytest ./test.py --pastebin=all
执行完毕后会生成一个seesion-log链接，打开即可

'''