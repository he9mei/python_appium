# encoding:utf-8  # 不加这个可能报错

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.implicitly_wait(10)


# <input id="kw" name="wd" class="s_ipt" value="今日新鲜事" maxlength="255" autocomplete="off">
# search_box = driver.find_element_by_id("kw")
# search_box = driver.find_element_by_name("wd")
# search_box = driver.find_element_by_class_name("s_ipt")
# search_box = driver.find_element_by_tag_name("input")   # 实用性低
# search_box = driver.find_element_by_xpath("/html/body/div/div/div/div/div/form/span/input")  # xpath 1.绝对路径定位
search_box = driver.find_element_by_xpath("//input[@id='kw']")  # xpath 2.利用元素属性定位 # 注意引号
search_box = driver.find_element_by_xpath("//input[@maxlength='255']")   # 任何属性都可以，只要能唯一标识
# xpath 3.层级与属性结合---待练习
# css_selector ---待练习

search_box.send_keys("selenium")

# <input type="submit" id="su" value="百度一下" class="bg s_btn">
search_bn = driver.find_element_by_id("su")
search_bn.click()


'''
# 验证link_text和partial_link_text---未验证通过，找不到
el_link = driver.find_element_by_link_text("关于百度")
# el_link = driver.find_element_by_partial_link_text()
'''

sleep(10)
driver.quit()
