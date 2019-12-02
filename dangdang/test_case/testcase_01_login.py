import time

from dangdang.base.base_prepare import BasePrepare, driver


def login():
    BasePrepare.set_up()
    driver.find_element_by_id("com.dangdang.reader:id/tab_personal_iv").click()
    time.sleep(5)
    BasePrepare.tear_down()


