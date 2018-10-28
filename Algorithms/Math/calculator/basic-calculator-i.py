#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-08 17:32:20
# File Name: calculate.py
# Description: Basic Calculator II
# LintCode: https://www.lintcode.com/problem/basic-calculator-ii/
#########################################################################
def calculate(s):
    res = 0
    num = 0
    n = len(s)
    op = '+'
    stack = []
    for i in range(0, n):
        if s[i] >= '0':
            num = num * 10 + int(s[i])
        if s[i] < '0' and s[i] != ' ' or i == n-1:
            if op == '+':
                stack.append(num)
            if op == '-':
                stack.append(-num)
            if op in ('*', '/'):
                pop_num = stack.pop()
                if op == '*':
                    push_num = pop_num * num
                if op == '/':
                    if pop_num < 0:
                        push_num = -((-pop_num) / num)
                    else:
                        push_num = pop_num / num
                stack.append(push_num)
            op = s[i]
            num = 0
        print stack
    while stack:
        res += stack.pop()
    return res

s = "3+2*2"
s = " 3/2 "
s = "1*2-3/4+5*6-7*8+9/10"
print calculate(s)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
