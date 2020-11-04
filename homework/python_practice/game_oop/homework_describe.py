# -*- coding: utf-8 -*-
# @Time    :2020/11/4 21:58
# @Author  :robot_zsj
# @File    :homework_describe.py
"""
作业1
用类和面向对象的思想，“描述”生活中任意接触到的东西（比如动物、小说里面的人物，
不做限制，随意发挥），数量为5个。
"""


# 圆形球类
class Ball:
    # 初始化球半径
    def __init__(self, radius):
        self.radius = radius

    # 对象用处
    def usage(self):
        pass


# 乒乓球
class TableTennis(Ball):
    # 重写对象用处
    def usage(self):
        print(f"My radius is {self.radius} cm, For Table Tennis games")


# 篮球类
class Basketball(Ball):
    # 重写对象用处
    def usage(self):
        print(f"My radius is {self.radius} cm, For basketball games")


# 排球类
class Volleyball(Ball):
    # 重写对象用处
    def usage(self):
        print(f"My radius is {self.radius} cm, For volleyball games")


# 足球类
class Football(Ball):
    # 重写对象用处
    def usage(self):
        print(f"My radius is {self.radius} cm, For Football games")


# 地球类
class Earth(Ball):
    # 重写对象用户处
    def usage(self):
        print(f"My radius is {self.radius} km, For human habitation")


if __name__ == '__main__':
    table_tennis = TableTennis(2)
    basketball = Basketball(22.5)
    football = Football(11.3)
    volleyball = Volleyball(10.35)
    earth = Earth(6371)
    table_tennis.usage()
    basketball.usage()
    football.usage()
    volleyball.usage()
    earth.usage()
