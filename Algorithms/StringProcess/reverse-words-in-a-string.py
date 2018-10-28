#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-22 13:11:51
# File Name: reverse-words-in-a-string.py
# Description: 翻转字符串
# LintCode: https://www.lintcode.com/problem/reverse-words-in-a-string/
#########################################################################
def reverseWords(s):
    s =s.strip(" ")
    print s
    mlist = s.split() 
    return " ".join(mlist[::-1])

s = "the sky is blue"
s = "  Life  doesn't  always    give     us  the       joys we want."
print reverseWords(s)
