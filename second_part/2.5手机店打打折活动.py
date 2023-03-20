#!/usr/bin/python
# -*- coding:utf-8 -*-
# @author  : micah
# @time    : 2023/3/20 17:22
# @function: 手机店在每周二的上午10点至11点和每周五的下午14点至15点，进行打折活动
# @version : 1.0

print("\n手机店正在打折，活动进行中。。。。。。")
strWeek = input("请输入中文日期（如星期一）：")
intTime = int(input("请输入时间中的小时（范围：0~23）"))
# 判断是否满足活动参与条件（使用了if条件语句）
if (strWeek == '星期二' and (10 <= intTime <= 11)) or (strWeek == '星期五' and (14 <= intTime <= 15)):
    print("恭喜您，获得了折扣活动参与资格，快快选购吧！")
else:
    print("对不起，您来晚了一步，期待下一次活动。。。。。。")


