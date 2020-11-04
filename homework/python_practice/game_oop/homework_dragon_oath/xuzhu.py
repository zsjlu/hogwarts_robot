# -*- coding: utf-8 -*-
# @Time    :2020/11/4 22:34
# @Author  :robot_zsj
# @File    :xuzhu.py
"""
1.定义一个XuZhu类，继承于童姥。虚竹宅心仁厚
不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
2.加入模块化改造
"""
import os
import sys
cpath = os.getcwd()
sys.path.append("cpath")
from tonglao import *


class XuZhu(TongLao):
    # 念经方法
    def read(self):
        print("罪过罪过")


if __name__ == '__main__':
    power, hp = random.choice(range(10, 21)), random.choice(range(2000, 4001))
    xuzu = XuZhu(hp=10000, power=500, name="虚竹")
    xuzu.read()
    xuzu.fight_zms(enemy_hp=hp, enemy_power=power)