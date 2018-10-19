#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-22 13:11:51
# File Name: bulb-switcher-ii.py
# Description: Bulb Switcher II
# LintCode: https://www.lintcode.com/problem/bulb-switcher-ii
#########################################################################
def flipLights(m, n):
    if m == 0 or n == 0:
        return 1
    if n == 1:
        return 2
    elif n == 2:
        if m == 1:
            return 3
        elif m > 1:
            return 4
    else:
        if m == 1:
            return 4
        elif m == 2:
            return 7
        elif m > 2:
            return 8

print flipLights(1, 2)
