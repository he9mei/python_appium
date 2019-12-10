

class gol:
    def init(self):#初始化
        global global_dict
        global_dict = {}

    def set_value(self,key,value):
        # 定义一个全局变量
        global_dict[key] = value

    def get_value(self,key,defValue=None):
        # 获得一个全局变量,不存在则返回默认值
        try:
            return global_dict[key]
        except KeyError:
            return defValue
