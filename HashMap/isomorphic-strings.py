#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-17 17:00:21
# File Name: isomorphic-strings.py
# Description: isomorphic-strings 
# LintCode: https://www.lintcode.com/problem/isomorphic-strings/
#########################################################################
def isIsomorphic(s, t):
    s_map = {}
    t_map = {}
    n = len(s)

    for i in range(n):
        if s_map.get(s[i]) != t_map.get(t[i]):
            return False
        s_map[s[i]] = i + 1
        t_map[t[i]] = i + 1
    return True

print isIsomorphic("abb", "egg")
print isIsomorphic("foo", "bar")
