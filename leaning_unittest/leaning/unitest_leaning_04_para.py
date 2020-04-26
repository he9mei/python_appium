'''
二、数据驱动
创建一个csv文件，写入百度搜索的数据。如何把搜索关键词参数化？
可以用读取到数据然后用for循环的方式（写在用例中），但是这样执行下来都包含在1条用例中，如果失败一个就都失败了；
改进后把for循环写在setUp中，然后在测试用例中安装索引取值，可以实现成多条用例，但是如果插入数据索引就会改变，也不方便。

1.parameterized
（1）parameterized安装
Parameterized是Python的一个参数化库，同时支持unittest、Nose和pytest单元测试框架。
GitHub地址：https://github.com/wolever/parameterized。
Parameterized支持pip安装。
-->pip3 install parameterized
安装失败，存在证书问题，更换为以下命令
# python3 -m  #没用这个
pip3 install parameterized --trusted-host=pypi.python.org --trusted-host=pypi.org --trusted-host=files.pythonhosted.org
用这个命令做了信任，安装成功啦！

（2）parameterized使用
---a.导入包---
from parameterized import parameterized
---b.在def函数前装饰---
@parameterized.expand([("case1","selenium"),("case2","appium"),("case3","unittest")])

实例见test_baidu_search_parameterized.py


2.DDT
DDT（Data-Driven Tests）是针对unittest单元测试框架设计的扩展库。允许使用不同的测试数据来运行一个测试用例，并将其展示为多个测试用例。
(1)ddt的安装
GitHub地址：https://github.com/datadriventests/ddt。
DDT支持pip安装:
pip3 install ddt
为了防止证书问题，加上信任
pip3 install ddt --trusted-host=pypi.python.org --trusted-host=pypi.org --trusted-host=files.pythonhosted.org
安装成功！

(2)ddt的使用---测试数据写在data()装饰器中
---a.导入包---
from ddt import ddt,data,file_data,unpack
---b.在类class之前装饰---
@ddt
---c.在函数def前装饰---
#有元组、列表、字典三种写法，都可以；注意字典的key要与测试方法的参数一致。
@data(("case1","selenium"),("case2","appium"))
# @data(["case1","selenium"],["case2","appium"])
# @data({"search_key":"selenium"},{"search_key":"appium"})
@unpack  #解包

实例见test_baidu_search_ddt_data.py

(3)ddt的使用---测试数据写在json文件中
---a.创建一个Json文件ddt_baidu_data.json---
{
	"case1":{"search_key":"selenium"},
	"case2":{"search_key":"appium"},
	"case3":{"search_key":"unittest"}
}
---b.在类class之前装饰---
@ddt
---c.在def函数前装饰---
# @file_data("ddt_baidu_data.json")  #需要把json文件放在测试用例同一个路径；否则需要带上路径。
@file_data("../data/ddt_baidu_data.yaml")
def test_search(self,search_key):  #测试用例参数传入search_key参数即可，无需再传入name
    self.baidu_search(search_key)  #直接使用search_key

实例见test_baidu_search_ddt_json.py

(4)ddt的使用---测试数据写在yaml文件中
---a.创建一个yaml文件ddt_baidu_data.yaml---
case1:
  - search_key: "selenium"
case2:
  - search_key: "appium"
case3:
  - search_key: "ddt"

---b.在类class之前装饰---
@ddt
---c.在def函数前装饰---
# @file_data("ddt_baidu_data.yaml")  #需要把yaml文件放在测试用例同一个路径；否则需要带上路径。
@file_data("../data/ddt_baidu_data.yaml")
def test_search(self,case):  #测试用例参数传入case
    search_key=case[0]["search_key"]   #从case获取search_key
    self.baidu_search(search_key)

出现问题：提示没有安装PyYAML，需要安装
pip3 install pyyaml --trusted-host=pypi.python.org --trusted-host=pypi.org --trusted-host=files.pythonhosted.org
安装出现问题：超时了
pip._vendor.urllib3.exceptions.ReadTimeoutError: HTTPSConnectionPool(host='files.pythonhosted.org', port=443): Read timed out.
解决超时问题：在命令后加上超时控制 --default-timeout=100
pip3 install pyyaml --trusted-host=pypi.python.org --trusted-host=pypi.org --trusted-host=files.pythonhosted.org --default-timeout=100
安装成功啦！

从yaml读取数据参数化成功！

实例见test_baidu_search_ddt_json.py
'''