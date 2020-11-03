# -*- coding: utf-8 -*-
# @Time    :2020/11/3 23:00
# @Author  :robot_zsj
# @File    :game_funny.py
"""
好玩的需求
"""
import random


def fight(enemy_hp, enemy_power):
    """
    :param enemy_hp: 敌人血量
    :param enemy_power: 敌人攻击力
    """
    # 定义2个变量存放数据,存放我的血量和攻击力
    my_hp = 1000
    my_power = 200

    # 加入循环，让游戏可以进行多轮fight
    while True:
        # 定义最终血量计算方式
        my_hp -= enemy_power
        enemy_hp -= my_power
        # 打印fight过程中血量变化
        print(f"我的血量 {my_hp},敌人血量{enemy_hp}")

        # 判断输赢谁的血量小于等于0，停止战斗！
        if my_hp <= 0:
            # 判断生命值低于零时，谁更低谁就输了
            print("我输了") if my_hp < enemy_hp else print("我赢了")
            break
        elif enemy_hp <= 0:
            # 判断生命值低于零时，谁更低谁就输了
            print("我输了") if my_hp < enemy_hp else print("我赢了")
            break


if __name__ == '__main__':
    # 利用列表推导式生成敌人hp
    hp = [ x for x in range(990, 1010)]
    # 敌人随机获得hp列表中的血量
    enemy_hp = random.choice(hp)
    print(f"敌人获得血量为 {enemy_hp}")

    # 敌人随机获得randint方法生成随机整数
    enemy_power = random.randint(190, 210)
    print(f"敌人获取攻击力为 {enemy_power}")

    # 传入敌人血量、攻击力，开始战斗！
    fight(enemy_hp, enemy_power)