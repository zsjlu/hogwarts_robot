# -*- coding: utf-8 -*-
# @Time    :2020/12/5 20:50
# @Author  :robot_zsj
# @File    :persional_edit.py
from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from homework.app.po_demo.page.base_page import BasePage
from homework.app.po_demo.page.find_contact_page import FindContactPage


class PersionalEdit(BasePage):

    _delete_confirm = (MobileBy.XPATH, f"//*[@text='确定']")

    def delete_member(self):
        sleep(5)
        self.find_by_scroll("删除成员").click()
        self.find(self._delete_confirm).click()
        return FindContactPage(self.driver)
