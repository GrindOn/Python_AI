#!/usr/bin/python
# -*- coding:utf-8 -*-
# @author  : micah
# @time    : 2023/3/19 18:23
# @function: a+b+c=1000,且a^2+b^2=c^2,求a,b,c.
# @version : 1.0

# 运行大约四分钟
for a in range(0, 1000):
    for b in range(0, 1000):
        for c in range(0, 1000):
            if a ** 2 + b ** 2 == c ** 2 and a + b + c == 1000:
                print("a,b,c:", a, b, c)

# 运行不到1分钟
for a in range(0, 1000):
    for b in range(0, 1000):
        c = 1000 -a - b
        if a ** 2 + b ** 2 == c ** 2:
            print("a,b,c:", a, b, c)
