'''
from pytest付费课程

五、pytest配置文件
pytest的配置文件通常放在测试目录下，名称为pytest.ini，命令行运行时使用该配置文件中的配置。
[pytest]  标志
addopts=-s  命令行运行参数，多个参数时空格隔开
testpaths=./scripts  测试搜索的路径，测试用例放在当前目录的scripts文件夹内
python_files=test_*.py  测试搜索的文件名，当前目录的scripts文件夹内，以test_开头，以.py结尾的所有文件
python_classes=Test_*  测试搜索的类名
python_functions=test_*  测试搜索的函数名

注意：pytest.ini文件不能有中文，中文注释也是不行的
选中项目，右键new-file，名称为pytest.ini保存即可
写入配置，如：
[pytest]
addopts=-s
testpaths=./leaning_pytest
python_files=test_06.py
python_classes=Test*
python_functions=test_*

配置好之后，再执行用例时修改即可，执行时只需要在pycharm的Terminal输入pytest即可。
'''