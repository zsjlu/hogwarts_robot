# -*- coding: utf-8 -*-
# @Time    :2020/11/7 12:29
# @Author  :robot_zsj
# @File    :03pytest__.py
# content of test_sample.py
import pytest
import yaml


print(yaml.safe_load(open("./data.yaml")))

def func(x):
    return x + 1


@pytest.fixture()
def login():
    return 'jerry'


def test_answer(login):
    print(login)
    assert func(3) == 5


@pytest.mark.parametrize('a, b', [(1, 2), (3, 4)])
def test_answer1(a, b):
    assert func(a) == b



@pytest.mark.parametrize('a, b', yaml.safe_load(open("./data.yaml")))
def test_answer2(a, b):
    assert func(a) == b

if __name__ == '__main__':
    pytest.main(['test_03.py::test_answer2', '-v'])