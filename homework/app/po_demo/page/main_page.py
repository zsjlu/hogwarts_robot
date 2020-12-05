# -*- coding: utf-8 -*-
# @Time    :2020/12/5 16:30
# @Author  :robot_zsj
# @File    :main_page.py


# adb shell dumpsys window|findstr mCurrentFocus
# >>>com.tencent.wework.launch.WwMainActivity
#
# 主页
from appium.webdriver.common.mobileby import MobileBy
from homework.app.po_demo.page.base_page import BasePage
from homework.app.po_demo.page.contact_list_page import ContactListPage

'''
主界面
'''


class MainPage(BasePage):
    _contact_list = (MobileBy.XPATH, "//*[@text='团队']")

    def goto_contactlist(self):
        """
        进入到团队
        :return:
        """
        self.find(self._contact_list).click()
        return ContactListPage(self.driver)
