# -*- coding: utf-8 -*-

# @File    : test.py
# @Date    : 2020-08-14
# @Author  : CuiMin

while True:
    try:
        x = int(input("input x number:"))
        break
    except ValueError:
        print("no number!")


# 同时处理多异常
try:
    x = abs(1+1)
except (RuntimeError, TypeError, NameError):
    pass


