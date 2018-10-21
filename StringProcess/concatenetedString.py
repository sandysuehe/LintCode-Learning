#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-22 13:11:51
# File Name: concatenetedString.py
# Description: 连接两个字符串中的不同字符 
# LintCode: https://www.lintcode.com/problem/concatenated-string-with-uncommon-characters-of-two-strings/
#########################################################################
def concatenetedString(s1, s2):
    hash_set = set()
    for i in s2:
        hash_set.add(i)

    hash_set1 = set()
    for j in s1:
        if j in hash_set:
            s1 = s1.replace(j, "")
            hash_set1.add(j)

    for k in s2:
        if k in hash_set1:
            s2 = s2.replace(k, "")
    return s1+s2
    
s1 = "aacdb"
s2 = "gafd"
s1 = "abcs"
s2 = "cxzca"
print concatenetedString(s1, s2)
