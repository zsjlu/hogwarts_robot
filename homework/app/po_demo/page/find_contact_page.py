# -*- coding: utf-8 -*-
# @Time    :2020/12/5 20:30
# @Author  :robot_zsj
# @File    :find_contact_page.py
from time import sleep
from appium.webdriver.common.mobileby import MobileBy
from homework.app.po_demo.page.base_page import BasePage
from homework.app.po_demo.page.persional_info import PersionalInfo

'''
查找联系人界面
'''

class FindContactPage(BasePage):

    count = 0

    def send_and_click(self, name):
        """
        输入姓名，等待人员显示，并点击第一个人员
        :param name:
        :return:
        """
        self.find((MobileBy.ID, "com.tencent.wework:id/fk1")).send_keys(name)
        sleep(2)
        # 输入姓名后等待查询列表展示
        eles = self.finds((MobileBy.XPATH, f"//*[@text='{name}']"))
        # 获取查询元素列表长度，小于1则说明没找到，直接退出
        FindContactPage.count = len(eles)
        if FindContactPage.count < 1:
            print("没有可删除的人员")
            return False
        print(FindContactPage.count)
        # 否则，点击第一个元素
        eles[1].click()
        return PersionalInfo(self.driver)

    def element_check(self, name):
        eles = self.finds((MobileBy.XPATH, f"//*[@text='{name}']"))
        afternum = len(eles)
        print(FindContactPage.count)
        return afternum == FindContactPage.count - 1

