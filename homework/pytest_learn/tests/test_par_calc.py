# -*- coding: utf-8 -*-
# @Time    :2020/11/15 12:16
# @Author  :robot_zsj
# @File    :test_par_calc.py
import allure
import pytest
import yaml
from homework.pytest_learn.core.test_method import Calc

# 加载yaml文件
def load_data(path='data2.yml'):
    with open(path) as f:
        data = yaml.safe_load(f)
        return data
# 根据测试的函数获取对应的数据
def commn_data_operate(args):
    keys = ",".join(args[0].keys())
    values = [list(d.values()) for d in args]
    case_data = {'keys': keys, 'values': values}
    return case_data

# 测试mul函数
class Test_Parm_Mul:
    data = load_data()
    case_data = commn_data_operate(data['mul'])

    def setup_class(self):
        self.calc = Calc()


    def teardown_class(self):
        pass

    def setup(self):
        pass

    def teardown(self):
        pass

    @pytest.mark.parametrize(case_data['keys'], case_data['values'])
    def test_mul(self, a, b, c):
        assert self.calc.mul(a, b) == c

# 测试div函数
class Test_Parm_Div:
    data = load_data()
    case_data = commn_data_operate(data['div'])

    def setup_class(self):
        self.calc = Calc()


    def teardown_class(self):
        pass

    def setup(self):
        pass

    def teardown(self):
        pass

    @pytest.mark.parametrize(case_data['keys'], case_data['values'])
    def test_div(self, a, b, c):
        assert self.calc.div(a, b) == c

