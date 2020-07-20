# 验证跨目录导入文件
# 1.将跨目录的文件路径加入系统路径，
# abspath(__file__)是当前路径的绝对路径
# dirname(path)表示path路径的上一级路径
import sys
from os.path import abspath, dirname

# project_path = dirname(dirname(abspath(__file__)))
# sys.path.append(project_path + "/page_object")
# append添加之后，sys.path没有加上，导入包还是找不到
# sys.path.insert(0,project_path+"/page_object")
# insert添加之后，sys.path加上了，但是只是临时的，导入包还是找不到

# 2.对LoginPage的导入做改写
# from po_appium_2.page_object.login_page import LoginPage
from login_page import LoginPage  # 永久添加page_object到sys.path之后，就可以直接导入了

# print(project_path + "/page_object")
print(sys.path)


''' 
补充1：查看sys.path                                                                                     
直接在python console，输入                                                                     
--> import sys                                                                           
-->sys.path                                                                              
能够显示已添加的路径，找到了项目路径'/Users/hehuaimei/PycharmProjects/python_appium'                       
所以从python_appium之下的路径开始找，也是可以的，比如：                                                       
po_appium_2.page_project.settings_page import SettingsPage                               

补充2：
dirname(__file__)和abspath(__file__)
# print(dirname(__file__))
# /Users/hehuaimei/PycharmProjects/python_appium/po_appium_2/test_case
# print(abspath(__file__))
# /Users/hehuaimei/PycharmProjects/python_appium/po_appium_2/test_case/learning_path.py

# print(dirname(dirname(__file__)))
# /Users/hehuaimei/PycharmProjects/python_appium/po_appium_2
# print(dirname(dirname(abspath(__file__))))
# /Users/hehuaimei/PycharmProjects/python_appium/po_appium_2

补充3：
临时添加路径到sys.path
sys.path.append(path)
sys.path.insert(0,path)

补充4：
永久添加路径到sys.path的3种方式：
1.将写好的py文件放到已有的sys.path路径下
2.在site-packages下面新建.pth文件，写入路径，一行一个路径
3.添加环境变量：
export PYTHONPATH=$PYTHONPATH:/Users/hehuaimei/PycharmProjects/python_appium/po_appium_2/page_object
注意，添加环境变量之后，需要重启python_appium工程，才会生效。否则from login_page import LoginPage还是报错。
'''