# -*- coding: utf-8 -*-
# @Time    :2020/12/7 20:22
# @Author  :robot_zsj
# @File    :mitmdump_maplocal.py
from mitmproxy import http

# request 方法名不能修改
def request(flow: http.HTTPFlow) -> None:
    # 发起请求，判断url是不是预期的值
    if flow.request.pretty_url == "https://www.baidu.com/":
        flow.response = http.HTTPResponse.make(
            200,  # (optional) status code
            b"Hello World",  # (optional) content
            {"Content-Type": "text/html"}  # (optional) headers
        )