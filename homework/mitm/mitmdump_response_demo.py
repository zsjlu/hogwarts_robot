# -*- coding: utf-8 -*-
# @Time    :2020/12/7 23:02
# @Author  :robot_zsj
# @File    :mitmdump_response_demo.py
from pprint import pprint

from mitmproxy import http


def response(flow: http.HTTPFlow):
    pprint(flow.response.content)
