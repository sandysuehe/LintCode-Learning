#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (hexue@4paradigm.com)
#########################################################################
# Created Time: 2018-08-22 16:42:33
# File Name: isOneEditDistance.py
# Description: 
#########################################################################
def isOneEditDistance(s, t):
    for i in range(0, min(len(s), len(t))):
        if s[i] != t[i]:
            if len(s) == len(t):
                return s[i+1:] == t[i+1:]
            elif len(s) < len(t):
                return s[i:] == t[i+1:]
            else:
                return s[i+1:] == t[i:]
    return abs(len(s)-len(t)) == 1

s="aDb"
t="adb"
print isOneEditDistance(s, t)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
