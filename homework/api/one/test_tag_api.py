# -*- coding: utf-8 -*-
# @Time    :2020/12/13 17:24
# @Author  :robot_zsj
# @File    :test_tag_api.py
import pytest
from homework.api.one.tag_api import TagApi


class TestTagAPi:

    def setup_class(self):
        # todo： 数据清理
        self.tag = TagApi()
        self.tag.get_token()

    # 每条案例之前清除数据
    def setup(self):
        r = self.tag.list()
        tag_group = r.json()['tag_group']
        if len(tag_group) != 0:
            self.group_tag_get(tag_group)
            self.data_delete(self.data)
            self.setup()

    # 获取标签
    def test_tag_list(self):
        # todo: 完善功能
        r = self.tag.list()
        assert r.json()['errcode'] == 0

    # 标签添加
    @pytest.mark.parametrize("group_name, tags_name", [
        ["group_1", [{"name": "robot1"}]],
        ["group_2", [{"name": "robot2"}]]

    ])
    def test_tag_add(self, group_name, tags_name):
        r = self.tag.list()
        assert r.json()['errcode'] == 0

        r = self.tag.add(group_name, tags_name)
        assert r.json()['errcode'] == 0

        r = self.tag.list()
        assert r.json()['errcode'] == 0

        group = [group for group in r.json()['tag_group'] if group['group_name'] == group_name][0]
        tags = [{'name': tag['name']} for tag in group['tag']]
        print(group)
        print(tags)
        assert group['group_name'] == group_name
        assert tags == tags_name

    # 标签删除
    @pytest.mark.parametrize("group_name, tags_name", [
        ["group_1", [{"name": "robot1"}]],
        ["group_2", [{"name": "robot2"}]]

    ])
    def test_tag_delete(self, group_name, tags_name):
        r = self.tag.add(group_name, tags_name)
        assert r.json()['errcode'] == 0

        r = self.tag.list()
        assert r.json()['errcode'] == 0
        tag_group = r.json()['tag_group']
        if len(tag_group) != 0:
            self.group_tag_get(tag_group)
            for group_id, tag_id in self.data.items():
                res = self.test_delete([group_id], tag_id)
                print(res)

    def test_update(self):
        pass

    def test_tag_add_fail(self):
        pass

    # 存储现有标签
    def group_tag_get(self, tag_group):
        g_id_dict = {}
        for item in tag_group:
            g_id = item['group_id']
            t_id_list = []
            for t in item['tag']:
                t_id_list.append(t['id'])
            g_id_dict[g_id] = t_id_list
        self.data = g_id_dict

    # 删除现有标签
    def data_delete(self, dict_data: dict):
        for group_id, tag_id in dict_data.items():
            self.test_delete([group_id], tag_id)

    # 删除标签
    def test_delete(self, group_id, tag_id):
        r = self.tag.delete(group_id, tag_id)
        # res = r.json()
        print(r.json())
        return r
