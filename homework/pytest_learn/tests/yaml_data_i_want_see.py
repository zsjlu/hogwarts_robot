# -*- coding: utf-8 -*-
# @Time    :2020/11/15 12:38
# @Author  :robot_zsj
# @File    :yaml_data_i_want_see.py
import yaml


def load_data(path='data2.yml'):
    with open(path) as f:
        data = yaml.safe_load(f)
        return data

def commn_data_operate(args):
    keys = ",".join(args[0].keys())
    values = [list(d.values()) for d in args]
    case_data = {'keys': keys, 'values': values}
    return case_data

data = load_data()

print(commn_data_operate(data['mul']))