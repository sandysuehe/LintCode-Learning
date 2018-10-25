#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-10-25 11:34:43
# File Name: valid-number.py
# Description: Valid Number 
# LintCode: https://www.lintcode.com/problem/valid-number/
#########################################################################
def isNumber(s):
    i = 0
    n = len(s)
    nums = list(s)

    isNum = False
    isDot = False
    isExp = False

    if s.isspace():   # 如果s是空格，False
        return False

    while i < n and nums[i].isspace: # 去掉头部的空格
        i += 1
    while n > i and nums[i].isspace: # 去掉尾部的空格
        n -= 1

    if nums[i] in ("+", "-"):
        i += 1

    while i < n:
        if nums[i].isdigit():
            isNum = True
        elif nums[i] == ".":
            if isExp or isDot:  # 遇到. 如果已经有.或者有e，False
                return False
            isDot = True
        elif nums[i] == "e":
            if isExp or not isNum: # 遇到e, 如果已经有e或者没有数字，False
                return False
            isExp = True
            isNum = False 
        elif nums[i] in ("+", "-"):
            if nums[i] != "e":
                return False
        else:
            return False
        i += 1
    return isNum
                
# vim: set noexpandtab ts=4 sts=4 sw=4 :
