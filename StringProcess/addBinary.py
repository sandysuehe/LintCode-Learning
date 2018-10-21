#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-28 16:28:08
# File Name: addBinary.py
# Description: 二进制求和
# LintCode: https://www.lintcode.com/problem/add-binary/
#########################################################################
def addBinary(a, b):
    ans = ""
    m = len(a) - 1
    n = len(b) - 1
    flag = 0

    while m >= 0 or n >= 0:
        if m >= 0:
            p = int(a[m])
            m -= 1
        else:
            p = 0

        if n >= 0:
            q = int(b[n])
            n -= 1
        else:
            q = 0

        val = (p + q + flag) % 2
        flag = (p + q + flag) / 2

        ans = str(val) + ans

    return ans if flag == 0 else "1"+ans


a = "11"
b = "1"
a = "0"
b = "0"
print addBinary(a, b)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
