# encoding:utf-8  # 不加这个可能报错

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.implicitly_wait(10)

print(driver.get_window_size())   # {'width': 1200, 'height': 783}
driver.set_window_size(800,400)   # 调整窗口大小，还可以最大化

# 输入框定位练习
# <input id="kw" name="wd" class="s_ipt" value="今日新鲜事" maxlength="255" autocomplete="off">

# search_box = driver.find_element_by_id("kw")  # id定位
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

# xpath 6.使用text()方法，匹配文本信息。可以达到link_text的效果；与contains结合，可以达到partial_link_text的效果。
# more_bn = driver.find_element_by_xpath("//a[text()='更多']")
# more_bn = driver.find_element_by_xpath("//a[contains(text(),'更')]")
# more_bn.click()
# sleep(2)

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
search_box = driver.find_element_by_css_selector("[class$='ipt']")  # $结尾

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


'''
# 验证link_text和partial_link_text---未验证通过，找不到
el_link = driver.find_element_by_link_text("关于百度")
# el_link = driver.find_element_by_partial_link_text()
'''

sleep(5)
driver.quit()
