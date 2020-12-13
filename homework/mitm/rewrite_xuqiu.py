# -*- coding: utf-8 -*-
# @Time    :2020/12/7 23:10
# @Author  :robot_zsj
# @File    :rewrite_xuqiu.py
import json
from mitmproxy import http


def response(flow: http.HTTPFlow):
    # 过滤条件
    if "quote.json" in flow.request.pretty_url and "x=" in flow.request.pretty_url:
        # 拿到响应数据， 转换为字典
        data = json.loads(flow.response.content)
        # 修改对应的字段的值
        data['data']['items'][0]['quote']['name'] = "rewrite_zsj"
        data['data']['items'][1]['quote']['name'] = "rewrite_zsjrewrite_zsj"
        data['data']['items'][2]['quote']['name'] = ""
        # 把修改后的数据， 转为字符串，赋值给原始响应数据
        flow.response.text = json.dumps(data)
