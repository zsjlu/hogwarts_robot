# -*- coding: utf-8 -*-
# @Time    :2020/12/5 16:43
# @Author  :robot_zsj
# @File    :contact_list_page.py.py

# 团队页面
from appium.webdriver.common.mobileby import MobileBy

from homework.app.po_demo.page.base_page import BasePage
from homework.app.po_demo.page.find_contact_page import FindContactPage
from homework.app.po_demo.page.member_invite_page import MemberInviteMenuPage

# 循环导入

'''
团队人员界面
'''


class ContactListPage(BasePage):
    # def __init__(self, driver:WebDriver):
    #     self.driver = driver
    _search = (MobileBy.XPATH,
               "//android.widget.RelativeLayout/android.widget.LinearLayout[2]/"
               "android.widget.RelativeLayout[1]/android.widget.TextView")

    def add_member(self):
        '''
        添加团队人员
        # 点击添加成员后跳转的activity：com.tencent.wework.friends.controller.MemberInviteMenuActivity
        :return:
        '''
        self.find_by_scroll("添加成员...").click()
        return MemberInviteMenuPage(self.driver)

    def find_member(self):
        """
        搜索
        :return:
        """
        self.find(self._search).click()
        return FindContactPage(self.driver)
