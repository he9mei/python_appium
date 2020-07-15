from po_appium_2.base.base_page import BasePage
from selenium.webdriver.common.by import By


class PersonalPage(BasePage):
    # el_tab_personal=(By.ID,"com.dangdang.reader:id/tab_personal_iv")
    el_tab_personal = (By.ID, "com.dangdang.reader:id/tab_personal_rl")
    el_nickname = (By.ID, "com.dangdang.reader:id/nickname_tv")  # 如果已登录，进入个人主页也是这个元素
    el_settings_enter=(By.ID, "com.dangdang.reader:id/common_menu_btn")




