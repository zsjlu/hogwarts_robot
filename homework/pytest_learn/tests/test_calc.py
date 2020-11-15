# -*- coding: utf-8 -*-
# @Time    :2020/11/15 11:08
# @Author  :robot_zsj
# @File    :test_suite01.py
import pytest
from homework.pytest_learn.core.test_method import Calc

@pytest.mark.skip
class Test_Suite():
    def setup_class(self):
        self.calc = Calc()

    def teardown_class(self):
        print("所有案例结束")

    def setup(self):
        pass

    def teardown(self):
        pass

    @pytest.mark.parametrize('a, b, c', [
        [1, 2, 2],
        [-1, -1, 1],
        [1, -1, 1],
        [0, 1, 0],
        [0.2, 1, 0.2],
        [0.2, 0.2, 0.04],
        [0.1, 0.2, 0.02]
    ])
    def test_mul(self, a, b, c):
        assert self.calc.mul(a, b) == c

    @pytest.mark.parametrize('a, b, c', [
        [1, 2, 0.5],
        [2, 1, 2],
        [-1, 1, 1],
        [1, -1, -1],
        [0.5, 1, 0.5],
        [1, 0.5, 2],
        [0, -1, 0],
    ])
    def test_div(self, a, b, c):
        assert self.calc.div(a, b) == c

    def test_div1(self):
        """除0, 报错除0错误"""
        try:
            self.calc.div(0, 2)
        except ZeroDivisionError as e:
            assert True
