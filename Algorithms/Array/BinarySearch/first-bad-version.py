#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-10-26 12:48:32
# File Name: first-bad-version.py
# Description: first-bad-version 
# LintCode: https://www.lintcode.com/problem/first-bad-version/
#########################################################################
def findFirstBadVersion(n):
    left = 1
    right = n

    while left + 1 < right:
        mid = (left+right)/2
        if SVNRepo.isBadVersion(mid):
            right = mid
        else:
            left = mid

    if SVNRepo.isBadVersion(left):
        return left
    return right
# vim: set noexpandtab ts=4 sts=4 sw=4 :
