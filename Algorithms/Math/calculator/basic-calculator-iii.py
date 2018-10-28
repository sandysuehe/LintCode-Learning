#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-08 17:32:20
# File Name: calculate.py
# Description: Basic Calculator III
# LintCode: https://www.lintcode.com/problem/basic-calculator-iii/
#########################################################################
def calculate(s):
    n = len(s)
    num = 0
    cur_res = 0
    res = 0
    operator = "+"

    for i in range(n):
        char = s[i]
        if char >= "0" and char <= "9":
            num = num * 10 + int(char)
        elif char == "(":
            j = i
            count = 0
            for i in range(j, n):
                if s[i] == "(":
                    count += 1
                if s[i] == ")":
                    count -= 1
                if count == 0:
                    break
            num = calculate(s[j+1:i])
            print s[j+1:i], "=", num
        if char in ("+", "-", "*", "/") or i==n-1:
            print "::::", cur_res, operator, num
            if operator == "+":
                cur_res += num
            if operator == "-":
                cur_res -= num
            if operator == "*":
                cur_res *= num
            if operator == "/":
                cur_res /= num

            if char in ("+", "-") or i==n-1:
                res += cur_res
                cur_res = 0

            operator = char
            num = 0

    return res

# s = "1 + 1"
# print s
# print calculate(s)
# 
# s = " 6-4 / 2 "
# print s
# print calculate(s)

s = "2*(5+5*2)/3+(6/2+8)"
print s
print calculate(s)

# s = "(2+6* 3+5- (3*14/7+2)*5)+3"
# print s
# print calculate(s)
