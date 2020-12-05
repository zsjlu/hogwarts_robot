# -*- coding: utf-8 -*-
# @Time    :2020/12/5 17:50
# @Author  :robot_zsj
# @File    :base_page.py


# 存放 driver的初始化，或者存放一些最基本的方法
import logging
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage:
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename='../log/myapp.log',
                        filemode='w')

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, locator):
        logging.info("find:")
        logging.info(locator)
        return self.driver.find_element(*locator)

    def finds(self, locator):
        logging.info("finds:")
        logging.info(locator)
        return self.driver.find_elements(*locator)

    def find_by_scroll(self, text):
        logging.info("find_by_scroll")
        logging.info(text)
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        'new UiScrollable(new UiSelector()'
                                        '.scrollable(true).instance(0))'
                                        '.scrollIntoView(new UiSelector()'
                                        f'.text("{text}").instance(0));')

    def get_toast_text(self):
        logging.info("get_toast:")
        result = self.find((MobileBy.XPATH, "//*[@class='android.widget.Toast']")).text
        logging.info(result)
        return result
