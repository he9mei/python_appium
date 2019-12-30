from appium_po.base.base_page import Base
from selenium.webdriver.common.by import By

class Common(Base):
    #通用返回按钮
    el_back_bn=(By.ID, "com.dangdang.reader:id/common_back")
    #特殊页面返回按钮---书吧详情页
    el_back_bn_bar=(By.ID, "com.dangdang.reader:id/bar_info_title_back")


