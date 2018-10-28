#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-10-16 12:09:28
# File Name: compare-version-numbers.py
# Description: Compare Version Numbers
# LintCode: https://www.lintcode.com/problem/compare-version-numbers/
#########################################################################
def compareVersion(version1, version2):
    n = len(version1) 
    m = len(version2)

    i = 0
    j = 0

    while i < n or j < m:
        carry_one = 0
        while i < n and version1[i].isdigit():
            carry_one = carry_one * 10 + int(version1[i])
            i += 1

        carry_two = 0
        while j < m and version2[j].isdigit():
            carry_two = carry_two * 10 + int(version2[j])
            j += 1

        if carry_one < carry_two:
            return -1
        elif carry_one > carry_two:
            return 1

        if  i < n and version1[i] == ".":
            i += 1

        if  j < m and version2[j] == ".":
            j += 1

        return 0

version1 = "0.1"
version2 = "1.1"
version1 = "1"
version2 = "01"
print compareVersion(version1, version2)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
