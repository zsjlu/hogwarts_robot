# -*- coding: utf-8 -*-
# @Time    :2020/12/5 16:53
# @Author  :robot_zsj
# @File    :contact_add_page.py


# 添加成员页面
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from homework.app.po_demo.page.base_page import BasePage
from homework.app.po_demo.page.member_invite_page import MemberInviteMenuPage

'''
联系人具体信息添加界面
'''


class ContactAddPage(BasePage):

    # def __init__(self, driver:WebDriver):
    #     self.driver = driver

    def edit_contact(self, name, gender, phonenum):
        '''
        编辑成员信息
        :return:
        '''
        self.find((MobileBy.XPATH, '//*[contains(@text, "姓名")]/../android.widget.EditText')).send_keys(
            name)
        self.find((MobileBy.XPATH, "//*[@text='性别']/..//*[@text='男']")).click()
        if gender == "男":
            WebDriverWait(self.driver, 10).until(lambda x: x.find_element(MobileBy.XPATH, "//*[@text='男']"))
            self.find((MobileBy.XPATH, "//*[@text='男']")).click()
        else:
            self.find((MobileBy.XPATH, "//*[@text='女']")).click()

        self.find((MobileBy.XPATH, "//*[@text='手机号']")).send_keys(phonenum)
        self.find((MobileBy.XPATH, "//*[@text='保存']")).click()
        return MemberInviteMenuPage(self.driver)
