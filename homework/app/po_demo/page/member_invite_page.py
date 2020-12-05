# -*- coding: utf-8 -*-
# @Time    :2020/12/5 16:48
# @Author  :robot_zsj
# @File    :member_invite_page.py
# from homework.app.po_demo.page.contact_add_page import ContactAddPage
# 循环导入
from appium.webdriver.common.mobileby import MobileBy

from homework.app.po_demo.page.base_page import BasePage

'''
添加方式选择页面
'''


class MemberInviteMenuPage(BasePage):

    # def __init__(self, driver:WebDriver):
    # self.driver = driver

    def add_member_manul(self):
        """
        点击手动添加成员进入activity：com.tencent.wework.contact.controller.ContactAddActivity
        :return:
        """
        self.find((MobileBy.XPATH, "//*[@text='手动输入添加']")).click()
        from homework.app.po_demo.page.contact_add_page import ContactAddPage
        # 局部导入，用到时才使用
        return ContactAddPage(self.driver)

    def verify_toast(self):
        result = self.get_toast_text()
        return result
