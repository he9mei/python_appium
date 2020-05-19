from selenium.common.exceptions import NoSuchElementException

from po_appium.base.base_page import Base
from selenium.webdriver.common.by import By
from po_appium.page_object.personal_page import Personal
from po_appium.page_object.common_page import Common
from time import sleep

class Settings(Base):
    el_logout_bn=(By.ID, "com.dangdang.reader:id/login")

    def settings_enter(self):
        self.click(*Personal.el_tab_personal)
        self.click(*Personal.el_settings_enter)

    # 这个退出主要是在登录之前调用，无论是否已登录，都无需报错。
    def logout(self):
        self.settings_enter()
        self.swipe_up(2)
        try:
            if self.is_displayed(*self.el_logout_bn):
                self.logger.info("用户已登录!")
                self.click(*self.el_logout_bn)
                self.get_toast("退出登录成功")
        except NoSuchElementException:
            self.logger.info("用户可能未登录！暂无法退出！")
        finally:
            self.click(*Common.el_back_bn)

    # 这个已登录判断，主要是在必须登录的页面case前，先确保已登录。如果未登录，需要报错。
    def is_login(self):
        self.settings_enter()
        self.swipe_up(2)
        try:
            if self.is_displayed(*self.el_logout_bn):
                self.logger.info("用户已登录!")
                return True
        except NoSuchElementException:
            self.logger.error("用户可能未登录！请先登录！")
            raise
            return False
        finally:
            self.click(*Common.el_back_bn)








