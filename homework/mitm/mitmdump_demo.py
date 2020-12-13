# -*- coding: utf-8 -*-
# @Time    : 2020/12/7 20:08
# @Author  : robot_zsj
# @File    : mitmdump_demo.py
from mitmproxy import http


def request(flow: http.HTTPFlow):
    flow.request.headers["myheader"] = "zsj"
    print(flow.request.headers)