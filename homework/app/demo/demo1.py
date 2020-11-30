# -*- coding: utf-8 -*-
# @Time    :2020/11/30 23:59
# @Author  :robot_zsj
# @File    :demo1.py.py
from time import sleep
from appium import webdriver

# 微信更新，修改了元素的定位信息，添加隐式等待
caps = {}
caps["platformName"] = "Android"
caps["deviceName"] = "hogwarts"
caps["appPackage"] = "com.tencent.wework"
caps["appActivity"] = ".launch.LaunchSplashActivity"
caps["noReset"] = "True"
# 最重要的代码，建立客户端与服务端的连接
driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
el1 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/"
    "android.widget.LinearLayout/android.widget.FrameLayout/"
    "android.widget.RelativeLayout/android.widget.LinearLayout/"
    "android.view.ViewGroup/android.widget.RelativeLayout[4]/android.widget.TextView")
driver.implicitly_wait(5)
el1.click()
el2 = driver.find_element_by_id("com.tencent.wework:id/guu")
el2.click()
el3 = driver.find_element_by_id("com.tencent.wework:id/fk1")
el3.send_keys("霍格沃兹测试1")
sleep(5)
driver.quit()
