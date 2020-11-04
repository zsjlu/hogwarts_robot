# -*- coding: utf-8 -*-
# @Time    :2020/11/4 22:34
# @Author  :robot_zsj
# @File    :tonglao.py
"""
定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。
TongLao类里面有2个方法，see_people方法，需要传入一个name参数，如果传入”WYZ”
（无崖子），则打印，“师弟！！！！”，如果传入“李秋水”，打印“师弟是我的！”，如果传
入“丁春秋”，打印“叛徒！我杀了你”fight_zms方法（天山折梅手），调用天山折梅手方法
会将自己的武力值提升10倍，血量缩减2倍。需要传入敌人的hp，power，进行一回合制对打，
打完之后，比较双方血量。血多的一方获胜。
"""
import random


# 天山童姥类
class TongLao:
    # 构造函数
    def __init__(self, hp: int, power: int, name: str="天山童姥"):
        """
        :param hp: 初始化生命值
        :param power: 初始化攻击力
        """
        self.hp = hp
        self.power = power
        self.name = name

    # 见到人后的反应
    def see_people(self, name: str):
        """
        :param name: 传入遇到的人名
        """
        # dict 人物：对应的话
        word = { "WYZ": "师弟！！！！", "李秋水": "师弟是我的！", "丁春秋": "叛徒！我杀了你" }
        # 这里是分割线
        print()
        print("*"*20)
        print(f"当天山童姥遇到了{name}")
        print()
        if name != "丁春秋":
            # 打印人物对应的话语
            print(f"天山童姥说：{word[name]}")
        else:
            # 打印人物对应的话语
            print(f"天山童姥说：{word[name]}")
            # 随机生成丁春秋的攻击力与生命值
            enemy_power, enemy_hp = random.choice(range(100, 201)), random.choice(range(1000, 2001))
            # 开始战斗，调用fight_zms()方法
            self.fight_zms(enemy_hp=enemy_hp, enemy_power=enemy_power)

    # 天山童姥武技：天山折梅手
    def fight_zms(self, enemy_hp: int, enemy_power: int):
        """
        :param enemy_hp: 敌人生命值
        :param enemy_power: 敌人攻击力
        """
        # 进入战斗开始框
        self.ready("<<战斗开始>>")
        # 天山童姥生命值减半，攻击力提升10倍
        self.hp /= 2
        self.power *= 10
        # 战斗一回合：天山童姥-敌人攻击力；敌人生命值-天山童姥攻击力
        self.hp -= enemy_power
        enemy_hp -= self.power
        # 展示战斗后的两人状态
        print(f"{self.name}状态：血量 {self.hp}, 攻击力 {self.power}")
        print(f"敌人状态：血量 {enemy_hp}, 攻击力 {enemy_power}")
        self.ready("<<战斗结束>>")
        # 通过血量判断胜负
        if self.hp == enemy_hp:
            print(f"{self.name}与敌人打成平手")
        else:
            print(f"{self.name}胜") if self.hp > enemy_hp else print("敌人胜")

    # 战斗框分隔，进入在当前后战斗后调用
    def ready(self, stage: str):
        print()
        # 打印当前战斗状态
        print(stage)
        print()


if __name__ == '__main__':
    power, hp = random.choice(range(10, 21)), random.choice(range(2000, 4001))
    tonglao = TongLao(power=power, hp=hp)
    tonglao.see_people("WYZ")
    tonglao.see_people("李秋水")
    tonglao.see_people("丁春秋")