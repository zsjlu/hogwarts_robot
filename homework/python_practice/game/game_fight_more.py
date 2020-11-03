# -*- coding: utf-8 -*-
# @Time    :2020/11/3 22:56
# @Author  :robot_zsj
# @File    :game_fight_more.py
"""
针对game_fight_one 模块中fight函数变为多回合
"""


def fight():
    # 定义4个变量存放数据
    my_hp = 1000
    my_power = 200
    enemy_hp = 1000
    enemy_power = 199

    # 加入循环，让游戏可以进行多轮fight
    while True:
        # 定义最终血量计算方式
        my_hp -= enemy_power
        enemy_hp -= my_power
        # 打印fight过程中血量变化
        print(f"我的血量 {my_hp},敌人血量{enemy_hp}")

        # 判断输赢谁的血量小于等于0，谁就输了
        if my_hp <= 0:
            print("我输了")
            break
        elif enemy_hp <= 0:
            print("我赢了")
            break


if __name__ == '__main__':
    # 函数调用
    fight()

