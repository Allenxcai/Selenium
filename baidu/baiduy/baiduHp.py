#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/18 15:31
# @Author  : Allen.XC.AI
# @File    : baiduHp.py

hello='hello world'
def add(a,b):
    return a+b
class index(object):
    def __init__(self):
        pass
    def add(self,a,b):
        return a+b

if __name__=="__main__":
    print(hello)
    print(add(2,3))
    demo=index()
    print(demo.add(3,4))