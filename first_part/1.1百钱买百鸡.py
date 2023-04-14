#!/usr/bin/python
# -*- coding:utf-8 -*-
# @author  : micah
# @time    : 2023/4/17 14:41
# @function: 公鸡5块，母鸡3块，雏鸡1块3只。用100块买100只
# @version :  4.14测试

for i in range(1, 20):
    for j in range(1, 33):
        for k in range(3, 99, 3):
            if i + j + k == 100 and 5 * i + 3 * j + k // 3 == 100:
                print("公鸡：", i, "母鸡：", j, "雏鸡：", k)
