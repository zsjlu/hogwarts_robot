# -*- coding: utf-8 -*-
# @Time    :2020/12/13 17:24
# @Author  :robot_zsj
# @File    :tag_api.py
"""


"""
import json
import requests

from homework.api.one.config_url import ConfigUrl

secret = 'Xg2J7QHltkklxvFmm-JK9LiKlCbn_VNeTwY_UZqYZ88'
id = 'wwcd5e1015ed2d9ab8'


# 调试代码
def test_get_token():
    r = requests.get(
        'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
        params={'corpid': id, 'corpsecret': secret})
    token = r.json()['access_token']
    return token


def test_tag_get():
    r = requests.post(
        "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
        params={'access_token': test_get_token()},
        json={
            'tag_id': []
        }
    )
    # print(r.json())
    # print(json.dumps(r.json(), indent=2))
    #
    # assert r.status_code == 200
    # assert r.json()['errcode'] == 0
    return r.json()


def test_tag_add():
    r = requests.post(
        'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag',
        params={'access_token': test_get_token()},
        json={
            # "group_id": "GROUP_ID",
            "group_name": "GROUP_NAME",
            "order": 1,
            "tag": [
                {
                    "name": "TAG_NAME_1",
                    "order": 1
                },
                {
                    "name": "TAG_NAME_2",
                    "order": 2
                }
            ]
        }
    )
    print(json.dumps(r.json(), indent=2))
    assert r.status_code == 200
    assert r.json()['errcode'] == 0

    return


# 业务接口
class TagApi:

    def __init__(self):
        self.url = ConfigUrl()
        self.token = ''

    def get_token(self):
        r = requests.get(
            self.url.TOKEN,
            params={'corpid': id, 'corpsecret': secret})
        token = r.json()['access_token']
        self.token = token

    def list(self):
        r = requests.post(
            self.url.LIST,
            params={'access_token': self.token},
            json={
                'tag_id': []
            }
        )
        return r

    def add(self, group_name, tags):
        r = requests.post(
            self.url.ADD,
            params={'access_token': test_get_token()},
            json={
                # "group_id": "GROUP_ID",
                "group_name": group_name,
                "order": 1,
                "tag": tags

            }
        )
        # print(json.dumps(r.json(), indent=2))
        # assert r.status_code == 200
        # assert r.json()['errcode'] == 0

        return r

    def update(self, old_new):
        """
        :param old_new: {
                        "id": "TAG_ID",
                        "name": "NEW_TAG_NAME",
                        "order": 1
                        }
        :return:
        """
        r = requests.post(
            self.url.UPDATE,
            params={'access_token': test_get_token()},
            json=old_new
        )
        return r

    def delete(self, group_id, tag_id):
        """
        :param group_id:{
                        "tag_id": [
                            "TAG_ID_1",
                            "TAG_ID_2"
                        ],
                        "group_id": [
                            "GROUP_ID_1",
                            "GROUP_ID_2"
                        ]
                    }
        :param tag_id:
        :return:
        """
        r = requests.post(
            self.url.DELETE,
            params={'access_token': test_get_token()},
            json={
                "group_id": group_id,
                "tag_id": tag_id
            }
        )
        return r
