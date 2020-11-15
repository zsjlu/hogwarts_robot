# -*- coding: utf-8 -*-
# @Time    :2020/11/15 14:27
# @Author  :robot_zsj
# @File    :test_contact_i_get_cookies.py
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWX:
    cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688851254523584'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'Ab5l11sjavDRMJna1I8DEpeQaiqF3K_4looJzB7mCPWVoeh3LCtx2Y_ZoCF8mcmgcYasqjFczoP0tJ7KiegSgTMbVJOssfzGx5-AgIafsEfmTem0FOewvnGWBxSPGjbq9RfWuHrUEXJKRlXE4cZgp5u-P0ZhThlXhfAA5XN_eHfQXEomPIWE5ow1SATpeaiEPyE8ONVxhFNybxgaRhoMER2N5XYx-2EZHW3kkYITWgYJqP3ZG8KKJns3QRs1gRtiQB4e2iLEDHeA4xQa66O8sQ'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688851254523584'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970324946198829'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'KOrpGoVidttSKkGM3NJ4QTaffjUKmVRWa4yB97WJS2nv0ipil2K_65v6f30XNokf'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a2697455'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1605423330'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '886408293330238'}, {'domain': 'work.weixin.qq.com', 'expiry': 1605450130.742055, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '5csjt4m'}, {'domain': '.qq.com', 'expiry': 1605509753, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.210404927.1605418613'}, {'domain': '.qq.com', 'expiry': 1668495353, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1941438552.1605418613'}, {'domain': '.work.weixin.qq.com', 'expiry': 1636954594.742096, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'expiry': 1608015413.706124, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path':'/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1636959330, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1605418597,1605422526,1605423330'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '1126817134'}, {'domain': '.qq.com', 'expiry': 2147483646.918626, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': '2dbd08c62193a091f7411e451ef5176723ff10e23c3ee34c9093a484c78f8224'}, {'domain': '.qq.com', 'expiry': 2147483649.483085, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': 'mRh4rZpSOf'}, {'domain': '.qq.com', 'expiry': 1607251848, 'httpOnly': False, 'name': 'ptui_loginuin', 'path': '/', 'secure': False, 'value': '940142834'}, {'domain': '.qq.com', 'expiry': 1920450645, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/', 'secure': False, 'value': '85ae9597dd4afd5f'}, {'domain': '.qq.com', 'expiry': 1605423466, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name':'pgv_pvi', 'path': '/', 'secure': False, 'value': '1828635648'}]


    def setup(self):
        option = Options()
        # 注意 9222 端口要与命令行启动的端口保持一致 --remote-debugging-port=9222
        option.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip()
    def test_case1(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.find_element(By.ID, "menu_contacts").click()

    def test_cookie_for_contact(self):
        # 打开首页
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # 去除cookie中的过期时间
        for cookie in self.cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        # 添加cookies后刷新页面
        self.driver.refresh()
        # 点击添加联系人按钮，输入信息，并确认
        self.driver.find_element(By.XPATH, '//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[1]/div/span[2]').click()
        self.driver.find_element(By.ID, 'username').send_keys('robot')
        self.driver.find_element(By.ID, 'memberAdd_acctid').send_keys('13052939116@qq.com')
        self.driver.find_element(By.ID, 'memberAdd_phone').send_keys('18166933948')
        self.driver.find_element(By.CSS_SELECTOR, '.js_btn_save').click()

        # 查看是否添加成功
        self.driver.find_element(By.XPATH, '//*[@id="menu_contacts"]/span').click()
        value = 'robot'
        locator = (By.CSS_SELECTOR, ".ww_checkbox")
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        sleep(2)
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        titles = [element.get_attribute("title") for element in elements]
        assert value in titles

    # def test_contact_delete(self):
    #     # 删除第一条记录
    #     # 打开首页
    #     self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    #     # 去除cookie中的过期时间
    #     for cookie in self.cookies:
    #         if 'expiry' in cookie.keys():
    #             cookie.pop('expiry')
    #         self.driver.add_cookie(cookie)
    #     # 添加cookies后刷新页面
    #     self.driver.refresh()
    #     self.driver.find_element(By.XPATH, '//*[@id="menu_contacts"]/span').click()
    #     sleep(5)
    #     locator = (By.CSS_SELECTOR, ".ww_checkbox")
    #     WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
    #     self.driver.find_element(By.CSS_SELECTOR, '.ww_checkbox:first').click()
    #     self.driver.find_element(By.CSS_SELECTOR, '.js_delete:last').click()

