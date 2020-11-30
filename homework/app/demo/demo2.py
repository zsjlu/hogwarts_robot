# -*- coding: utf-8 -*-
# @Time    :2020/12/1 0:01
# @Author  :robot_zsj
# @File    :demo2.py
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class TestWX:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "True"
        # 最重要的代码，建立客户端与服务端的连接
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(30)

    def teardown(self):
        self.driver.quit()

    # @pytest.mark.skip()
    def test_contact(self):
        logging.basicConfig(level=logging.INFO)
        name = "hogwarts_00001"
        gender = "男"
        phonenum = "13812121214"
        # 点击【团队】

        self.driver.find_element(MobileBy.XPATH, "//*[@text='团队']").click()
        # 点击【添加成员】

        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("添加成员...").instance(0));').click()
        # 点击【手动输入添加】
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text, "姓名")]/../android.widget.EditText').send_keys(
            name)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='性别']/..//*[@text='男']").click()
        if gender == "男":
            self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        else:
            self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()

        self.driver.find_element(MobileBy.XPATH, "//*[@text='手机号']").send_keys(phonenum)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成功']").click()
        result = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        assert result == "添加成功"
        # sleep(2)
        # print(self.driver.page_source)

    # @pytest.mark.skip()
    def test_delcontact(self):
        name = "hogwarts_00001"
        # 点击【团队】
        self.driver.find_element(MobileBy.XPATH, "//*[@text='团队']").click()
        # 点击【搜索】图标
        self.driver.find_element(MobileBy.XPATH,
                                 "//android.widget.RelativeLayout/android.widget.LinearLayout[2]/"
                                 "android.widget.RelativeLayout[1]/android.widget.TextView").click()
        # self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/dqn").click()
        # resource-id 方式
        # 定位输入框并输入姓名
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/fk1").send_keys(name)
        sleep(2)
        # 输入姓名后等待查询列表展示
        eles = self.driver.find_elements(MobileBy.XPATH, f"//*[@text='{name}']")
        # 获取查询元素列表长度，小于1则说明没找到，直接退出
        beforenum = len(eles)
        if beforenum < 1:
            print("没有可删除的人员")
            return
        # 否则，点击第一个元素
        eles[1].click()
        # 点击 右上角的按钮
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/guk").click()
        self.driver.find_element(MobileBy.XPATH, f"//*[@text='编辑成员']").click()
        # self.driver.find_element(MobileBy.XPATH, f"//*[@text='删除成员']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("删除成员").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, f"//*[@text='确定']").click()
        sleep(2)
        eles1 = self.driver.find_elements(MobileBy.XPATH, f"//*[@text='{name}']")
        afternum = len(eles1)
        assert afternum == beforenum - 1

