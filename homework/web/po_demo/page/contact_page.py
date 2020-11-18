# -*- coding: utf-8 -*-
# @Time    :2020/11/18 21:39
# @Author  :robot_zsj
# @File    :contact_page.py
from homework.web.po_demo.page.web_base import Web_Base
from selenium.webdriver.common.by import By
import time


class Contact_Page(Web_Base):
    # 删除联系人列表中第一个元素
    def delete_member(self):
        # 勾选框定位第一个元素的定位
        locater = (By.XPATH, '//*[@id="member_list"]/tr[1]/td[1]/input')
        # 判断元素是否可点击
        self.wait_for_click(locater)
        # 勾选元素
        # 等待一下
        time.sleep(2) # 页面元素加载过快，容易点不到
        self.find(*locater).click()
        # 点击删除
        self.driver.find_element(By.XPATH, '//*/div/div[2]/div/div[2]/div[3]/div[1]/a[3]').click()
        # 删除确认
        self.driver.find_element(By.XPATH, '//*[@id="__dialog__MNDialog__"]//div[3]/a[1]').click()
        # 当前企业人数
        time.sleep(2)
        number = self.driver.find_element(By.XPATH, '//*//span/span/span[2]')
        # 返回
        return number
