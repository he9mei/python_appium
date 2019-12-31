from selenium.common.exceptions import NoSuchElementException

from appium_po.base.base_page import Base
from selenium.webdriver.common.by import By
from appium_po.page_object.personal_page import Personal
from appium_po.page_object.common_page import Common
from time import sleep

class Settings(Base):
    el_logout_bn=(By.ID, "com.dangdang.reader:id/login")

    def settings_enter(self):
        self.click(*Personal.el_tab_personal)
        self.click(*Personal.el_settings_enter)

    def logout(self):
        self.settings_enter()
        self.swipe_up(2)
        try:
            if self.is_displayed(*self.el_logout_bn):
                # print("找到退出登录按钮!")
                self.logger.info("找到退出登录按钮!")
                self.click(*self.el_logout_bn)
                self.wait(2)
        except NoSuchElementException:
            # print(e)
            # print("找不到退出按钮，可能目前未登录。")
            self.logger.info("找不到退出按钮，可能目前未登录。")
        finally:
            self.click(*Common.el_back_bn)







