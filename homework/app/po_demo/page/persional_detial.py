# -*- coding: utf-8 -*-
# @Time    :2020/12/5 20:46
# @Author  :robot_zsj
# @File    :persion_detial.py
from appium.webdriver.common.mobileby import MobileBy
from homework.app.po_demo.page.base_page import BasePage


class PersionalDetial(BasePage):

    _edit_element = (MobileBy.XPATH, f"//*[@text='编辑成员']")

    def edit_persion_info(self):
        self.find(self._edit_element).click()
        from homework.app.po_demo.page.persional_edit import PersionalEdit
        return PersionalEdit(self.driver)
