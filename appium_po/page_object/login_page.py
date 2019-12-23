from selenium.webdriver.common.by import By
from appium_po.base.base_page import Base

class Login_page(Base):
    #元素
    el_tab_personal=(By.ID,"com.dangdang.reader:id/tab_personal_iv")
    el_login_enter=(By.ID,"com.dangdang.reader:id/nickname_tv")
    el_custom_login_enter=(By.ID,"com.dangdang.reader:id/custom_login_tv")
    el_name_input=(By.ID,"com.dangdang.reader:id/name_edit")
    el_pw_input=(By.ID,"com.dangdang.reader:id/password_et")
    el_login_bn=(By.ID,"com.dangdang.reader:id/login_tv")


    def custom_login_enter(self):
        self.click(self.el_tab_personal)
        self.click(self.el_login_enter)
        self.click(self.el_custom_login_enter)

    def custom_login(self):
        self.send_keys(self.el_name_input,"18500228275")
        self.send_keys(self.el_pw_input,"111111")
        self.driver.press_keycode(4)  #点击登录时虚拟键盘没有自动关闭
        self.click(self.el_login_bn)



'''


os.system("adb shell ime set io.appium.android.ime/.UnicodeIME")

el3 = driver.find_element_by_id("com.dangdang.reader:id/name_edit")
el3.clear()
el3.send_keys("18500000005")
el4 = driver.find_element_by_id("com.dangdang.reader:id/password_et")
el4.clear()
el4.send_keys("111111")

#遇到问题：输入之后，键盘没有关闭，挡住了登录按钮


el5 = driver.find_element_by_id("com.dangdang.reader:id/login_tv")
el5.click()

'''
