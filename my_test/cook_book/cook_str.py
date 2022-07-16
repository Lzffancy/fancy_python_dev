# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: cook book 案例测试
Desc :
"""
import os

line = 'asdf fjdk; afed, fjek,asdf, foo'
import re

print(re.split(r'[;,\s]\s*', line))
print(re.findall(r'[;,\s]\s*', line))

filenames = os.listdir(".")
print(filenames)
print(list((name for name in filenames if name.endswith(".py"))), "python文件")

a = 3
b = 2
c = 1
print(a, b, c, sep="===")

# float
print(bin(a))
print(oct(a))
print(hex(a))

print("======")
x = 1234
x_b = format(x, "b")
print(x_b)

print(int(x_b, 2))

print(str(["123"][0]))
