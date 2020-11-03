# -*- coding: utf-8 -*-
# @Time    :2020/11/3 22:50
# @Author  :robot_zsj
# @File    :game_fight.py
"""
需求：

一个回合制游戏，每个角色都有hp和power，hp代表血量，power代表攻击力
hp的初始值为1000，power的初始值为200，
定义一个fight方法：
my_final_hp = my_hp - enemy_power
my_final_hp = enemy_hp - my_power
两个hp进行比对，血量剩余多的人获胜
"""


def fight():
    # 定义4个变量存放数据
    my_hp = 1000
    my_power = 200
    enemy_hp = 1000
    enemy_power = 199

    # 定义最终血量计算方式
    my_hp -= enemy_power
    enemy_hp -= my_power
    # 打印敌我血量
    print(f"我的血量 {my_hp},敌人血量{enemy_hp}")

    # 判断输赢
    # 使用三目运算符
    print("我赢了") if my_hp > enemy_hp else print("我输了")


if __name__ == '__main__':
    # 函数调用
    fight()
