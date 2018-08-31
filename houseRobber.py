#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (hexue@4paradigm.com)
#########################################################################
# Created Time: 2018-08-27 19:19:02
# File Name: houseRobber.py
# Description: 
#########################################################################
def houseRobber(num):
    if len(num) == 0:
        return 0
    if len(num) == 1:
        return num[0]
    if len(num) == 2:
        return max(num[0], num[1])

    pre = num[0]
    cur = num[1]
    for i in range(2, len(num)):
        res = max(num[i]+pre, cur)
        pre = cur
        cur = res
    return res


num = [3, 8, 4]
num = [3, 8, 4, 5]
print houseRobber(num)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
