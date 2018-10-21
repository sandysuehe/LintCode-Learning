#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-08 17:32:20
# File Name: calculate.py
# Description: Basic Calculator
# LintCode: https://www.lintcode.com/problem/basic-calculator/
#########################################################################
def calculate(s):
    res = 0
    sign = 1
    num = 0
    n = len(s)
    stack = []

    for i in range(0, n):
        if s[i] >= '0':
            num = num * 10 + int(s[i])
            print num
        else:
            res += sign * num
            num = 0
            if s[i] == "+":
                sign = 1
            if s[i] == "-":
                sign = -1
            if s[i] == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            if s[i] == ")":
                pop_sign = stack.pop()
                res *= pop_sign
                pop_num = stack.pop()
                res += pop_num
        if i == n - 1:
            res += sign * num
    return res

s = "(1+(4+5+2)-3)+(6+8)"
s = " 2-1 + 2 "
s = "2-4-(8+2-6+(8+4-(1)+8-10))"
#s = "1 + 1"
print calculate(s)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
