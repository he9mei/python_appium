'''
三、pytest 运行模式---插件
1.运行后生成测试报告-2

pytest+allure模式
----------------------
（1）环境搭建
mac端：pytest+allure环境搭建
已经安装：
jdk1.8
Python3.8
Pycharm
Mac已经安装homebrew

1.安装pytest
—>pip3 install -U pytest

2.安装allure
（1）下载
—>brew install allure
结果：下载失败
手动下载：https://dl.bintray.com/qameta/maven/io/qameta/allure/allure-commandline/2.13.0/allure-commandline-2.13.0.zip
下载完成后，找到bin目录下的allure.bat 双击打开
（2）然后配置环境变量：
#配置allure的路径
export PATH=$PATH:/Users/hehuaimei/Downloads/allure-2.13.0/bin
（3）验证是否安装成功
—>allure —version
结果：2.13.0

3.安装allure-pytest
—>pip3 install allure-pytest
结果：安装成功 allure-pytest-2.8.6

注意：还有一个插件是pytest-allure-adaptor，这个和allure-pytest只需要安装一个，如果同时安装的话，运行的时候会出现错误。
这两者的区别官网上给出的解释如下所示:
pytest-allure-adaptor
主要命令:
$ py.test --alluredir [path_to_report_dir] //生成报告
allure-pytest
这边使用的是allure-pytest，主要命令：
$ py.test --alluredir = %allure_result_folder% //生成报告
$ allure serve %allure_result_folder% //查看报告

问题：
1.安装pytest成功后，在终端还是无法识别pytest命令。
解决：到pycharm代码中import pytest会提示安装pytest，安装成功后，终端还是无法识别，但是pycharm的Terminal可以识别。
2.pycharm的Terminal执行 pytest --alluredir命令无法识别
解决：到pycharm的Terminal重新执行了pip3 install allure-pytest，安装了2次成功了，可以识别了。

------------------------------------------------
（2）运行
-->pytest --alluredir=%allure_result_folder%  #生成报告---这个文件里面都是各个用例分开的结果不能直接打开报告
-->allure serve %allure_result_folder%  #打开报告
#可以打开一个html报告，如 http://192.168.142.91:49991/index.html
问题：
以上serve打开报告，之后再打开还需要这样操作比较麻烦，可以使用以下命令，生成index.html

-->allure generate ./report/allure_report/ -o ./report/allure_report/html --clean
或者
-->allure generate ./report/allure_report/ -c -o ./report/allure_report/html

结果：Report successfully generated to ./report/allure_report/html
操作后index.html即会放在./report/allure_report/html路径下
备注:
./report/allure_report/ 是之前生成的allure结果的文件的路径
./report/allure_report/html 是根据之前生成的allure结果的文件再生成index.html的存放路径，可以自己绝对存放位置
--clean 如果html这个路径已经存在，则先删除html文件。
也可以写成-c
------------------------------------------------
'''