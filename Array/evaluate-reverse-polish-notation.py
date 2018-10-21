#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-09 18:33:04
# File Name: evalRPN.py
# Description: 逆波兰表达式求值
# LintCode: https://www.lintcode.com/problem/evaluate-reverse-polish-notation/
#########################################################################
def evalRPN(s):
    stack = []
    for item in s:
        if item not in ["+", "-", "/", "*"]:
            stack.append(int(item))
        else:
            num1 = stack.pop()
            num2 = stack.pop()
            if item == "+":
                stack.append(num2+num1)
            elif item == "-":
                stack.append(num2-num1)
            elif item == "*":
                stack.append(num2*num1)
            elif item == "/":
                if num2*num1 < 0:
                    stack.append(-((-num2)/num1))
                else:
                    stack.append(num2/num1)
    return stack.pop()

s = ["2", "1", "+", "3", "*"]
s = ["4", "13", "5", "/", "+"]
print evalRPN(s)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
