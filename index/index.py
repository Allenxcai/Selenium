#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/18 15:40
# @Author  : Allen.XC.AI
# @File    : index.py
# from baidu.baiduHp import hello, add, index
from baidu.baiduHp import *

if __name__ == "__main__":
    print(hello)
    print(add(2, 3))
    demo = index()
    print(demo.add(3, 3))
