# -*- coding: utf-8 -*-
# @Time    :2020/11/17 22:32
# @Author  :robot_zsj
# @File    :add_member_page.py
from homework.web.po_demo.page.contact_page import Contact_Page
from homework.web.po_demo.page.web_base import Web_Base
from selenium.webdriver.common.by import By


class Add_Member_Page(Web_Base):

    def add_member(self, name, account, phonenum):
        # 注册成员
        self.find(By.ID, "username").send_keys(name)
        self.find(By.ID, "memberAdd_acctid").send_keys(account)
        self.find(By.ID, "memberAdd_phone").send_keys(phonenum)
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        return self

    def get_member(self, value):
        """
        这里我不用添加太多的成员，我这里会及时删除，所以这个不用
        :param value:
        :return:
        """
        # 勾选按钮定位
        locator = (By.CSS_SELECTOR, ".ww_checkbox")
        self.wait_for_click(locator)
        # 放置多个页面的姓名列表
        titles_total = []
        while True:
            # 获取成员中的所有名字
            elements = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
            # 列表生成式，当前页面所有成员的姓名
            titles = [element.get_attribute("title") for element in elements]
            # 寻找预期姓名， 找到返回True
            if value in titles:
                return True
            # 当前页面没有找到，将当前页面姓名列表添加到所有页面的列表
            titles_total.extend(titles)
            # 获取当前页面与总页面
            page: str = self.find(By.CSS_SELECTOR, ".ww_pageNav_info_text").text
            # 分割当前页面与总页面
            num, total = page.split("/", 1)
            # 当前页面与总页面相等，返回False
            if int(num) == int(total):
                return False
            else:
                # 否则点击下一页操作
                self.find(By.CSS_SELECTOR, ".ww_commonImg_PageNavArrowRightNormal").click()


    def goto_contact_page(self):
        # 点击进入通讯录列表
        self.driver.find_element(By.XPATH, '//*[@id="menu_contacts"]/span').click()
        return Contact_Page(self.driver)
