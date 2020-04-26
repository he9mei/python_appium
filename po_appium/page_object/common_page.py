from po_appium.base.base_page import Base
from selenium.webdriver.common.by import By

class Common(Base):
    #通用返回按钮
    el_back_bn=(By.ID, "com.dangdang.reader:id/common_back")

    #以下是非通用返回按钮
    #书吧详情页
    el_back_bn_bar=(By.ID, "com.dangdang.reader:id/bar_info_title_back")
    #登录页
    el_back_bn_login=(By.ID,"com.dangdang.reader:id/back_iv")




