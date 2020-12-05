# -*- coding: utf-8 -*-
# @Time    :2020/12/5 16:57
# @Author  :robot_zsj
# @File    :test_contact.py
from homework.app.po_demo.page.app import App


class TestWX:
    def setup_class(self):
        self.app = App()

    def setup(self):
        self.main = self.app.start().goto_main()

    def test_addcontact(self):
        name = "hogwarts_00001"
        gender = "男"
        phonenum = "13812121214"
        result = self.main.goto_contactlist().add_member().add_member_manul().edit_contact(name, gender,
                                                                                           phonenum).verify_toast()
        assert "添加成功" == result

    def test_deletecontact(self):
        name = "hogwarts_00001"
        result = self.main.goto_contactlist().find_member()\
            .send_and_click(name).goto_persion_detial()\
            .edit_persion_info().delete_member().element_check(name)
        assert result

    def teardown_class(self):
        self.app.stop()
