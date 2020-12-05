# -*- coding: utf-8 -*-
# @Time    :2020/12/5 20:40
# @Author  :robot_zsj
# @File    :persion_info.py
from appium.webdriver.common.mobileby import MobileBy
from homework.app.po_demo.page.base_page import BasePage
from homework.app.po_demo.page.persional_detial import PersionalDetial

'''
个人简介信息界面
'''


class PersionalInfo(BasePage):

    _persional_info = (MobileBy.ID, "com.tencent.wework:id/guk")

    def goto_persion_detial(self):

        self.find(self._persional_info).click()

        return PersionalDetial(self.driver)