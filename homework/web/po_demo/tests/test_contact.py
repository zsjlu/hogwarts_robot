# -*- coding: utf-8 -*-
# @Time    :2020/11/17 22:43
# @Author  :robot_zsj
# @File    :test_contact.py
from time import sleep

import pytest

from homework.web.po_demo.page.index_page import Index_Page


class TestContact:
    def setup_class(self):
        self.index = Index_Page().add_cookies()

    def teardown_class(self):
        self.index.quit()

    # @pytest.mark.skip()
    def test_addcontact(self):
        name = "aa_0"
        account = "aa_0_hogwarts"
        phonenum = "13911111111"

        add_member_page = self.index.click_add_member()
        result = add_member_page.add_member(name, account, phonenum)
        result.goto_contact_page()
        # 调试
        sleep(5)
        # 这里返回的是添加联系人界面实例对象了
        assert  isinstance(result, object)

    # @pytest.mark.skip()
    def test_delete_first(self):
        result = self.index.contact_manage().delete_member()
        assert result

    # 对页面添加成员并删除
    @pytest.mark.skip()
    def test_add_delete_contact(self):
        name = "aa_0"
        account = "aa_0_hogwarts"
        phonenum = "13911111111"

        add_member_page = self.index.click_add_member()
        result1 = add_member_page.add_member(name, account, phonenum).goto_contact_page().delete_member()
        assert result1
