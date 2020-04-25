
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# from time import sleep,strftime,localtime,time
import time
import os
import random

from appium_po.conftest import caps
# from appium_po.base.log_conf import Log
import logging

class Base(object):
    def __init__(self, driver,logger):
        self.driver=driver
        # self.driver=webdriver.Remote("http://localhost:4723/wd/hub",caps)  #跑用例需要注释掉
        print(f"传入Base的driver是：{self.driver}")
        # self.logger=Log(self.__class__.__name__) #通过base下的log_conf.py文件内的配置，设置log---放在不同文件
        self.logger=logger  #通过log.conf文件内的配置+conftest.py文件接收配置，设置log---放在同一个文件
        # self.logger=logging.getLogger()   #跑用例需要注释掉

#定位元素、点击、输入、判断是否存在
    def locator_element(self, *locator):
        '''定位元素'''
        try:
            el=self.driver.find_element(*locator)
            return el
        except NoSuchElementException:
            # print(f"找不到元素：{locator}")
            self.logger.error("找不到元素："+str(locator))

    def click(self, *locator):
        self.locator_element(*locator).click()
        # print(f"点击元素:{locator}")
        self.logger.info("点击元素：" + str(locator))
        '''
        # 验证问题：找元素是已经做了异常处理，每一个方法封装时还需要做异常处理吗？以下是出现异常时的情况
        总结：不需要再做异常处理
        try:
            # if self.driver.find_element(*locator).is_displayed():  # 找不到元素，无法点击  passed
            # if self.locator_element(*locator).is_displayed(): #找不到元素 failed (与以上不加异常处理，效果相同)
            if self.is_displayed(*locator):  # 找不到元素，无法点击  passed
                self.locator_element(*locator).click()
                 # print(f"点击元素:{locator}")
                self.logger.info("点击元素:"+str(locator))
        except NoSuchElementException:
            self.logger.info("找不到元素，无法点击")
        '''

    def send_keys(self, text, *locator):
        self.sys_input_method("appiumUnicode")
        self.locator_element(*locator).clear()
        self.locator_element(*locator).send_keys(text)
        # print(f"元素：{locator} 输入：{text}")
        self.logger.info("元素："+str(locator)+" 输入："+text)
        # self.sys_input_method("baidu")  #输入之后切换到百度输入法，不切回去也行

    def is_displayed(self, *locator):
        try:
            # if self.driver.find_element(*locator).is_displayed():
            assert self.driver.find_element(*locator).is_displayed()
            # print(f"元素出现:{locator}")
            self.logger.info("元素出现："+str(locator))
            return True
        # except NoSuchElementException:
        except AssertionError:
            # print(f"元素未出现:{locator}")
            self.logger.error("元素未出现："+str(locator))
            return False

#获取元素list、按照index点击、随机点击
    def locator_elements(self, *locator):
        '''定位元素list'''
        try:
            el_list=self.driver.find_elements(*locator)
            return el_list
        except NoSuchElementException:
            self.logger.error("找不到元素："+str(locator))

    def click_index(self,index,*locator):
        el_list=self.locator_elements(*locator)
        el_list[index].click()
        self.logger.info("按序号点击元素["+str(index)+"]："+str(locator))

    def click_random(self,*locator):
        el_list=self.locator_elements(*locator)
        n=len(el_list)  #len(list)获取列表长度
        index=random.randint(0,n-1)  #生成列表长度内的随机数;random.randint(a,b) 包含 a和b
        el_list[index].click()
        self.logger.info("随机点击元素["+str(index)+"]："+str(locator))

#截图、获取toast
# 注意点：
# 1、给定截图的名称为中文，则需添加u，如：get_screenShot(u"个人主页")，否则截图保存的文件名称乱；---貌似不写也没问题
# 2、若给定的截图名称为英文，则不需添加U
    def get_screenshot(self,name):
        day=time.strftime("%Y-%m-%d",time.localtime(time.time()))
        # tm=time.strftime("%Y-%m-%d_%H_%M_%S",time.localtime(time.time()))  #图片文件名加上日期和时间
        tm=time.strftime("%H_%M_%S",time.localtime(time.time()))  #由于文件夹是以日期命名的，文件名省去日期
        fq="../test_result/screentshot/"+day
        try:
            if os.path.exists(fq):
                filename=fq+"/"+tm+"_"+name+".png"
            else:
                os.makedirs(fq)
                filename=fq+"/"+tm+"_"+name+".png"
            self.driver.get_screenshot_as_file(filename)
            self.logger.info("截图成功："+name)
        except Exception as e:
            self.logger.error("截图失败:"+name)
            print(e)

    def get_toast(self,text):
        try:
            el_toast=(By.XPATH,"//*[contains(@text,'"+text+"')]")
            self.logger.info("el_toast："+str(el_toast))
            ele=WebDriverWait(self.driver,10,0.1).until(EC.presence_of_element_located(el_toast))
            self.logger.info("获取toast值为："+ele.text)
            return ele.text
        except TimeoutException:
            self.logger.error("获取toast失败-time out")


#断言文字(gettext,iscontains等等)？

#三种等待：强制等待、隐式等待、显示等待
    # @staticmethod
    def wait(self,t):
        '''强制等待'''
        time.sleep(t)
        # print(f"等待{t}s")
        self.logger.info("等待："+str(t)+"s")

    def implicitly_wait(self,t):
        '''隐式等待'''
        self.driver.implicitly_wait(t)
        # print(f"隐式等待{t}s")
        self.logger.info("隐式等待："+str(t)+"s")

    def explicitly_wait(self,t,locator):
        '''显式等待'''
        #此处locator不需要定义为*,源代码_find_element(driver, by)就直接使用的locator，貌似直接可以接收元组。
        try:
            el=WebDriverWait(self.driver,t,0.5).until(EC.visibility_of_element_located(locator))
            # print(f"显式等待-元素出现：{locator}")
            self.logger.info("显式等待-元素出现："+str(locator))
            return el
        except NoSuchElementException:
            # print(f"显示等待-元素未出现：{locator}")
            self.logger.info("显示等待-元素未出现："+str(locator))
        except TimeoutException:
            # print("显示等待-time out")
            self.logger.info("显示等待-time out")

#切换手机系统输入法，实际相当于是在终端输入相应命令，利用os.system
    @staticmethod
    def sys_input_method(method_name):
        '''切换手机系统的输入法'''
        if method_name=="appiumUnicode":
            os.system("adb shell ime set io.appium.android.ime/.UnicodeIME")
        if method_name=="baidu":
            os.system("adb shell ime set com.baidu.input_huawei/.ImeService")

#滑动：向上、向下、向左、向右滑动，向上滑动到某个元素
    def swipe_up(self,n=1,t=500):
        s=self.driver.get_window_size()
        # print(f"屏幕尺寸是：{s}")
        start_x = s['width']*1/2
        start_y = s['height']*4/5
        end_x = s['width']*1/2
        end_y = s['height']*1/5
        for i in range(n):
            self.driver.swipe(start_x,start_y,end_x,end_y,t)
            # print(f"向上滑动第{i+1}次")
            self.logger.info("向上滑动第"+str(i+1)+"次")
            self.wait(1)

    def swipe_down(self,n=1,t=500):
        s=self.driver.get_window_size()
        # print(f"屏幕尺寸是：{s}")
        start_x = s['width']*1/2
        start_y = s['height']*1/5
        end_x = s['width']*1/2
        end_y = s['height']*4/5
        for i in range(n):
            self.driver.swipe(start_x,start_y,end_x,end_y,t)
            # print(f"向下滑动第{i+1}次")
            self.logger.info("向下滑动第" + str(i + 1) + "次")
            self.wait(1)

    def swipe_left(self,n=1,t=500):
        s=self.driver.get_window_size()
        # print(f"屏幕尺寸是：:{s}")
        start_x=s['width']*4/5
        start_y=s['height']*1/2
        end_x=s['width']*1/5
        end_y=s['height']*1/2
        for i in range(n):
            self.driver.swipe(start_x,start_y,end_x,end_y,t)
            # print(f"向左滑动第{i+1}次")
            self.logger.info("向左滑动第" + str(i + 1) + "次")
            self.wait(1)

    def swipe_right(self,n=1,t=500):
        s = self.driver.get_window_size()
        # print(f"屏幕尺寸是：:{s}")
        start_x = s['width'] * 1/5
        start_y = s['height'] * 1/2
        end_x = s['width'] * 4/5
        end_y = s['height'] * 1/2
        for i in range(n):
            self.driver.swipe(start_x, start_y, end_x, end_y, t)
            # print(f"向右滑动第{i+1}次")
            self.logger.info("向右滑动第" + str(i + 1) + "次")
            self.wait(1)

    # def swipe_up_to_el(self,t=100,*locator):  #默认值参数后面跟不定长参数，出错了。。。
    def swipe_up_to_el(self, *locator):
        '''向上滑动直到找到某个元素'''
        s=self.driver.get_window_size()
        # print(f"屏幕尺寸是：:{s}")
        start_x=s['width']*1/2
        start_y=s['height']*8/10
        end_x=s['width']*1/2
        end_y=s['height']*5/10
        t=500

        for i in range(20):
            try:
                if self.driver.find_element(*locator).is_displayed():
                    # print(f"滑动到元素-成功:{locator}")
                    self.logger.info("滑动到元素-成功："+str(locator))
                    break
            except NoSuchElementException:
                # print("滑动到元素-元素暂未出现")
                self.logger.info("滑动到元素-元素暂未出现")
            self.driver.swipe(start_x,start_y,end_x,end_y,t)
            # print(f"滑动到元素-向上缓慢滑动第{i+1}次")
            self.logger.info("滑动到元素-向上缓慢滑动第"+str(i+1)+"次")
        else:
            # print(f"滑动到元素-失败:{locator}")
            self.logger.info("滑动到元素-失败：" + str(locator))
        self.wait(1)

