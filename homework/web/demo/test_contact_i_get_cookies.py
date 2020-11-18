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

# @pytest.mark.skip()
class TestWX:
    cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688851254523584'}, {'domain': '.work.weixin.qq.com', 'h\
ttpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'vkWKVuNXSAjnQ0j5BIbJ-c0tf1D44zromttyaOnRFD97TFsi2HMUJi00WDMxbcEwK5TyfYjMtx7Ie6k6WKXXpU7beYuYyXRyskdIjOI6Ajszi4G\
ncM-hPW-evQvF8HmM-QTmtLD7iTTQ-xD2fMjsZUi2WlTo1RiyxgxsM_QqQZCr5Cn9BL8kfpz--Ahls58R7ZUGpCeUebZ4AknA4WgwvjZB3UGvOKHZvGypQ59G_KX6z5BIAXtrTbdjUcCIgYFV0QoC74u_3Ia8c5VJ5N-6tQ'}, {'domain': '.work\
.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688851254523584'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.cor\
pid', 'path': '/', 'secure': False, 'value': '1970324946198829'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'KOrpGoVid\
ttSKkGM3NJ4QT1KE0T2FaOjL3O63Ejt6TTTD78Bcxi87omipn-IXkUW'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a5600768'}, {'\
domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '35151860392028930'}, {'domain': 'work.weixin.qq.com', 'expiry': 1605734063,\
 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '60radjg'}, {'domain': '.qq.com', 'expiry': 1605711089, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secur\
e': False, 'value': 'GA1.2.1587430255.1605624688'}, {'domain': '.qq.com', 'expiry': 1668696689, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1941438552.1\
605418613'}, {'domain': '.work.weixin.qq.com', 'expiry': 1636954594, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.work.weixin.qq.com\
', 'expiry': 1608294876, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype\
', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.work\
.weixin.qq.com', 'expiry': 1637238701, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1605422526,1605423330,1605624687,160570\
2528'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '1126817134'}, {'domain': '.qq.com', 'expiry': 2147483648,\
 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': '2dbd08c62193a091f7411e451ef5176723ff10e23c3ee34c9093a484c78f8224'}, {'domain': '.qq.com', 'expiry': 2147483649,\
'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': 'mRh4rZpSOf'}, {'domain': '.qq.com', 'expiry': 1608131898, 'httpOnly': False, 'name': 'ptui_loginuin', 'path': '/',\
'secure': False, 'value': '940142834'}, {'domain': '.qq.com', 'expiry': 1920450645, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/', 'secure': False, 'value': '85ae9597dd4afd5f'},\
 {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': False, 'value': '1828635648'}]


    def setup(self):
        option = Options()
        # 注意 9222 端口要与命令行启动的端口保持一致 --remote-debugging-port=9222
        # option.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()
        pass

    @pytest.mark.skip()
    def test_case1(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.find_element(By.ID, "menu_contacts").click()

    @pytest.mark.skip()
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
        sleep(1)
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        titles = [element.get_attribute("title") for element in elements]
        assert value in titles

    def test_contact_delete(self):
        # 删除第一条记录
        # 打开首页
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # 去除cookie中的过期时间
        for cookie in self.cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        # 添加cookies后刷新页面
        self.driver.refresh()
        # 点击进入通讯录列表
        self.driver.find_element(By.XPATH, '//*[@id="menu_contacts"]/span').click()
        sleep(2)
        locator = (By.XPATH, '//*[@id="member_list"]/tr[1]/td[1]/input')
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(By.XPATH, '//*[@id="member_list"]/tr[1]/td[1]/input').click()
        self.driver.find_element(By.XPATH, '//*/div/div[2]/div/div[2]/div[3]/div[1]/a[3]').click()
        self.driver.find_element(By.XPATH, '//*[@id="__dialog__MNDialog__"]//div[3]/a[1]').click()
        number = self.driver.find_element(By.XPATH, '//*//span/span/span[2]')
        sleep(2)
        assert "1人" in number.text


