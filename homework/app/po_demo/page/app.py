# -*- coding: utf-8 -*-
# @Time    :2020/12/5 16:27
# @Author  :robot_zsj
# @File    :app.py.py

# app.py 存放app相关的操作，启动app，关闭app，重启app，计入到主页
from appium import webdriver
from homework.app.po_demo.page.base_page import BasePage
from homework.app.po_demo.page.main_page import MainPage


class App(BasePage):

    def start(self):
        if self.driver == None:
            print("driver == None")
            caps = {}
            caps["platformName"] = "Android"
            caps["deviceName"] = "hogwarts"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.LaunchSplashActivity"
            caps["noReset"] = "True"
            # 最重要的代码，建立客户端与服务端的连接
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self.driver.implicitly_wait(5)
        else:
            print("driver is not None")
            # 启动app, 启动的页面是desirecaps 里面设置的activity,这里时caps["appActivity"]
            self.driver.launch_app()
            # self.driver.start_activity("com.tencent.wework",".launch.LaunchSplashActivity")
            # 这里需要给定参数
        return self

    def restart(self):
        pass

    def stop(self):
        self.driver.quit()

    # 通过这个方法跳转到主页
    def goto_main(self):
        return MainPage(self.driver)