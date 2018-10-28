#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-22 13:11:51
# File Name: isValidParentheses.py
# Description: Valid Parentheses 验证括号 
# LintCode: https://www.lintcode.com/problem/valid-parentheses/ 
#########################################################################
def isValidParentheses(s):
    stack = []
    for char in s:
        if char in ("{", "[", "("):
            stack.append(char)
        else:
            if not stack:
                return False
            if char == "]" and stack[-1] != "[":
                return False
            if char == ")" and stack[-1] != "(":
                return False
            if char == "}" and stack[-1] != "{":
                return False
            stack.pop()
    return not stack 


#s = "()[]{}"
s = "([)]"
s = "]"
s = "([{}])"
s = "["
print isValidParentheses(s)
