# -*- coding: utf-8 -*-
# @Time    :2020/11/17 22:32
# @Author  :robot_zsj
# @File    :index_page.py
from selenium.webdriver.common.by import By

from homework.web.po_demo.page.add_member_page import Add_Member_Page
from homework.web.po_demo.page.contact_page import Contact_Page
from homework.web.po_demo.page.web_base import Web_Base


class Index_Page(Web_Base):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

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


    # def __init__(self):
    #     option = Options()
    #     option.debugger_address = "127.0.0.1:9222"
    #     self.driver = webdriver.Chrome(options=option)
    #     self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    def add_cookies(self):
        for cookie in self.cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        # 添加cookies后刷新页面
        self.driver.refresh()
        return self

    # 添加成员
    def click_add_member(self):
        self.find(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)").click()
        return Add_Member_Page(self.driver)

    # 成员列表
    def contact_manage(self):
        # 点击进入通讯录列表
        self.driver.find_element(By.XPATH, '//*[@id="menu_contacts"]/span').click()
        return Contact_Page(self.driver)