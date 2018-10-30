#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-10-26 10:19:16
# File Name: guess-number-higher-or-lower.py
# Description: Guess Number Higher or Lower 
# LintCode: https://www.lintcode.com/problem/guess-number-higher-or-lower/
#########################################################################
def guessNumber(n):
    left = 1
    right = n

    while left < right:
        mid = (left + right) / 2
        ans = guess(mid)

        if ans == 0:
            return mid
        elif ans == -1:
            right = mid - 1
        else:
            left = mid + 1
    return -1



n = 10
print guessNumber(n)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
