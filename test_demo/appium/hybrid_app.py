from appium import webdriver
from time import sleep

caps={
    "automationName":"UIAutomator2",
    "platformName":"Android",
    # "platformVersion":"7.1.1",
    # "deviceName":"MJA68TGES4S4SKAY",  # oppo
    # "platformVersion": "8.0.0",
    # "deviceName":"HMKNW17727007061",  # 华为lite
    "platformVersion": "9",
    "deviceName":"GEY6R20507024610",  # 华为play

    "appPackage":"com.dangdang.reader",
    "appActivity":".activity.GuideActivity",
    "noReset":True,
    "unicodeKeyboard":True,
    "resetKeyboard":True
}

'''
查看acicity较为简单的方法：
抓app的日志-->adb logcat>/Users/hehuaimei/Desktop/log_test.text
然后搜索dispalyed即可看到以下内容
Displayed com.dangdang.reader/.activity.GuideActivity
'''

driver=webdriver.Remote("http://localhost:4723/wd/hub",caps)
driver.implicitly_wait(10)

# 进入书城tab
el_book_store_tab=driver.find_element_by_id("com.dangdang.reader:id/tab_store_iv")
el_book_store_tab.click()

# 进入书城tab-电子书
print("进入书城tab-电子书")
# els_book_store_top=driver.find_elements_by_class_name("android.support.v7.app.ActionBar$Tab")
# els_book_store_top[1].click()
# 以上定位list有问题

# 定位电子书tab方法2，使用content-desc
el_book_store_top=driver.find_element_by_accessibility_id("电子书")

#获得当前上下文
current_context=driver.current_context
print(f"当前上下文：{current_context}")

#获得所有上下文
all_contexts=driver.contexts
for context in all_contexts:
    print(context)

#切换上下文到WEBVIEW---只有华为play切换成功了
# driver.switch_to.context("WEBVIEW_com.dangdang.reader")
driver.switch_to.context("WEBVIEW_xweb")
print(f"切换之后的上下文：{driver.current_context}")

# 操作电子书webview内容
# 点击查看更多
el_more=driver.find_element_by_class_name("more")
el_more.click()
sleep(2)

# 切回上下文到NATIVE_APP
driver.switch_to.context("NATIVE_APP")
print(f"切换之后的上下文：{driver.current_context}")

# 返回
el_back=driver.find_element_by_id("com.dangdang.reader:id/common_back")
el_back.click()

sleep(5)
driver.quit()