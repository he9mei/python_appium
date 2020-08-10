# encoding:utf-8  # 不加这个可能报错

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.implicitly_wait(10)

# 窗口大小获取和设置练习
size = driver.get_window_size()
print(size)   # {'width': 1200, 'height': 783}
# driver.maximize_window()  # 窗口最大化
driver.set_window_size(1200,400)   # 设置窗口大小

# 输入框定位练习
# <input id="kw" name="wd" class="s_ipt" value="今日新鲜事" maxlength="255" autocomplete="off">

search_box = driver.find_element_by_id("kw")  # id定位
# search_box = driver.find_element_by_name("wd")  # name定位
# search_box = driver.find_element_by_class_name("s_ipt")  # class_name定位
# search_box = driver.find_element_by_tag_name("input")   # tag_name定位

# xpath 1.绝对路径定位
# search_box = driver.find_element_by_xpath("/html/body/div/div/div/div/div/form/span/input")

# xpath 2.利用元素属性定位，注意引号，任何属性都可以，只要能唯一标识。如果不想指定标签名，可以用*代替。
# search_box = driver.find_element_by_xpath("//input[@id='kw']")
# search_box = driver.find_element_by_xpath("//input[@maxlength='255']")
# search_box = driver.find_element_by_xpath("//*[@class='s_ipt']")

# xpath 3.层级与属性结合,可以从上一级或者上上级的唯一属性来定位
# search_box = driver.find_element_by_xpath("//span[@class='bg s_ipt_wr iptfocus quickdelete-wrap']/input")
# search_box  = driver.find_element_by_xpath("//form[@id='form']/span/input")

# xpath 4.使用逻辑运算符and
# search_box = driver.find_element_by_xpath("//input[@name='wd' and @class='s_ipt']")

# xpath 5.使用contains匹配一个属性中包含的字符串
# span的实际class="bg s_ipt_wr iptfocus quickdelete-wrap"
# search_box = driver.find_element_by_xpath("//span[contains(@class,'s_ipt_wr')]/input")
# 这里注意格式，如果使用@class='s_ipt_wr'会报错

# xpath 6.使用text()方法，匹配文本信息。可以达到link_text的效果；
# 与contains结合，可以达到partial_link_text的效果。
'''
# 用进入更多页面来练习
# more_bn = driver.find_element_by_xpath("//a[text()='更多']")
# more_bn = driver.find_element_by_xpath("//a[contains(text(),'更')]")

# link_text和partial_link_text练习
# more_bn=driver.find_element_by_link_text("更多")
more_bn=driver.find_element_by_partial_link_text("更")
more_bn.click()
sleep(2)
'''

# css_selector
# css_selector 1.通过id定位
# search_box = driver.find_element_by_css_selector("#kw")    # #id

# css_selector 2.通过class定位
# search_box = driver.find_element_by_css_selector(".s_ipt")  # .class

# css_selector 3.通过标签名定位
# search_box = driver.find_element_by_css_selector("input")  # selenium.common.exceptions.ElementNotInteractableException: Message: element not interactable

# css_selector 4.通过标签层级关系定位
# search_box = driver.find_element_by_css_selector("span>input")

# css_selector 5.通过属性定位
# search_box = driver.find_element_by_css_selector("[name='wd']")

# css_selector 6.组合定位
# search_box = driver.find_element_by_css_selector("span.bg s_ipt_wr quickdelete-wrap>input")  # 这个class貌似这样用不了
# search_box = driver.find_element_by_css_selector("form#form>span>input")

# css_selector 7.更多定位方法
# search_box = driver.find_element_by_css_selector("[class='s_ipt']")
# search_box = driver.find_element_by_css_selector("[class*='s_ipt']")  # *包含
# search_box = driver.find_element_by_css_selector("[class^='s_i']")  # ^开头
# search_box = driver.find_element_by_css_selector("[class$='ipt']")  # $结尾

'''
top_bn = driver.find_element_by_css_selector("div>div:nth-child(3)>a:nth-child(5)")  #指定标签下第几个
top_bn.click()
sleep(2)
driver.back()  进入百度贴吧后不支持返回，关于页面的back()和forword()再单独练习
'''

search_box.send_keys("selenium")

# <input type="submit" id="su" value="百度一下" class="bg s_btn">
search_bn = driver.find_element_by_id("su")
search_bn.click()
sleep(2)

'''
# 页面的前进和后退练习
# 如果没有打开新的窗口，可以直接通过后退和前进切换页面
driver.back()
# driver.forward()
# driver.refresh()

# 多窗口切换练习
handle1 = driver.current_window_handle
print(f"当前窗口title是：{driver.title}")
driver.find_element_by_link_text("更多").click()  # 进入更多页，会打开新窗口
sleep(2)
# 如果打开新窗口，可以通过driver.switch_to.window()切换窗口
driver.switch_to.window(handle1)
driver.find_element_by_link_text("学术").click()  # 进入学术页，会打开新窗口
sleep(2)
driver.switch_to.window(handle1)

all_handles = driver.window_handles
for handle in all_handles:
    if handle != handle1:
        driver.switch_to.window(handle)
        sleep(2)
        print(f"for循环切换后的窗口title是：{driver.title}")
        driver.close()  # 关闭当前窗口
driver.switch_to.window(handle1)
'''

# 截图练习
# filename="/Users/hehuaimei/Desktop/png/baidu.png"
# driver.save_screenshot(filename)
# driver.get_screenshot_as_file(filename)  # 这两种写法都可以

# 获取验证信息
# title=driver.title  # 获取当前页面标题
# current_url=driver.current_url  # 获取当前页面url
# num_text=driver.find_element_by_css_selector(".nums_text").text   # 获取某元素的文本信息
# print(f"当前页面title是:{title}")
# print(f"当前url是:{current_url}")
# print(f"搜索结果条数信息是：{num_text}")  # 能找到，此处文字是在span之间


# webdriver常用方法
# driver.back()
# result=driver.find_element_by_css_selector("#kw").is_displayed()  # 元素是否可见
# attribute=driver.find_element_by_css_selector("#kw").get_attribute("name")  # 获取元素的属性值，如name
# input_box_size=driver.find_element_by_css_selector("#kw").size   # 获取输入框大小
# text=driver.find_element_by_xpath("//a[@class='s-bri c-font-normal c-color-t' and @name='tj_briicon']").text  # 获取元素文字
# print(f"元素是否出现:{result}")
# print(f"属性值是:{attribute}")
# print(f"输入框大小是:{input_box_size}")
# print(f"文字是:{text}")  # 能找到，此处文字在a标签之间

# 键盘操作练习，可以通过keys来输入键盘上的按键，包含全选/复制/剪贴/粘贴等
# driver.back()
# driver.find_element_by_id("kw").send_keys("seleniumm")
# sleep(1)
# driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)  #删除
# sleep(1)
# driver.find_element_by_id("kw").send_keys(Keys.SPACE)  #空格
# sleep(1)
# driver.find_element_by_id("kw").send_keys(Keys.CONTROL,"a")
# sleep(1)
# # driver.find_element_by_id("kw").send_keys(Keys.CONTROL,"x")
# driver.find_element_by_id("kw").send_keys(Keys.CONTROL,"c")
# sleep(1)
# driver.find_element_by_id("kw").send_keys(Keys.CONTROL,"v")
# sleep(1)
# driver.find_element_by_id("kw").send_keys(Keys.ENTER)

'''
# 定位1组元素
driver.back()
# 这样获得的是第1个a标签，不是一组
# els=driver.find_element_by_xpath("//div[@id='s-top-left']/a")
# els=driver.find_element_by_css_selector("div#s-top-left>a")
# print(els.text)
# web如何获得一组元素？find_elements_by_8大元素定位
# els=driver.find_elements_by_xpath("//div[@id='s-top-left']/a")
els=driver.find_elements_by_css_selector("div#s-top-left>a")
print(len(els))  # 打印元素列表的个数
for el in els:
    print(el.text)  # 打印该div下的所有a标签的text
'''
'''
# 操作cookie
# 获取所有cookies
# all_cookies=driver.get_cookies()
# print(f"操作之前的cookie是：{all_cookies}")
# 删除所有cookies
# driver.delete_all_cookies()
# print(f"操作之后的cookie是：{driver.get_cookies}")
# 添加cookie字典，必须指定name和value
driver.add_cookie({'name':'cookie_name_hahahha','value':'cookie_value_hahaha'})
print("添加后的cookie：")
for cookie in driver.get_cookies():
    print("%s-->%s"%(cookie["name"],cookie["value"]))
# 根据cookie_name查看cookie_value
cookie_value=driver.get_cookie(name='cookie_name_hahahha')
print(f"name为cookie_name_hahahha的cookie的值是：{cookie_value}")
# 根据cookie_name删除cookie
driver.delete_cookie(name="cookie_name_hahahha")
print("删除后的cookie：")
for cookie in driver.get_cookies():
    print("%s-->%s"%(cookie["name"],cookie["value"]))
'''

# 鼠标操作，如鼠标悬停
# driver.back()
# more_bn=driver.find_element_by_link_text("更多")
# action=ActionChains(driver)
# action.move_to_element(more_bn).perform()

# （滑动解锁---暂不验证）
# 上下滑动选择时间---待验证
# 可以用ActionChains类实现，这里用TouchActions类中的scroll_from_element()


sleep(5)
driver.quit()
