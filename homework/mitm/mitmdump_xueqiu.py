# -*- coding: utf-8 -*-
# @Time    :2020/12/7 22:23
# @Author  :robot_zsj
# @File    :mitmdump_xueqiu.py
from mitmproxy import http

# request 方法名不能修改
def request(flow: http.HTTPFlow) -> None:
    # 发起请求，判断url是不是预期的值
    if "quote.json" in flow.request.pretty_url:
        with open("data.json", encoding="utf-8") as f:
            flow.response = http.HTTPResponse.make(
                200,  # (optional) status code
                # 读取文件中的数据作为返回内容
                f.read(),
                {"Content-Type": "application/json"}  # (optional) headers
            )