#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-10-16 19:16:09
# File Name: wildcard-matching.py
# Description: Wildcard Matching 外卡匹配 
# LintCode: https://www.lintcode.com/problem/wildcard-matching/
#########################################################################
# 思路: 
# 星号跟前面的字符没有半毛钱关系，如果前面的字符没有匹配上，那么直接返回false了，根本不用管星号。
# 而星号存在的作用是可以表示任意的字符串，当然只是当匹配字符串缺少一些字符的时候起作用，
# 当匹配字符串包含目标字符串没有的字符时，将无法成功匹配。
#########################################################################
def isMatch(s, p):
    m = len(s)
    n = len(p)
    dp = [[False for i in range(n+1)] for j in range(m+1)]
    dp[0][0] = True

    for i in range(1, n+1):
        if p[i-1] == "*":
            dp[0][i] = dp[0][i-1]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if p[j-1] == "*":
                dp[i][j] = dp[i-1][j] or dp[i][j-1]
            else:
                dp[i][j] = (s[i-1] == p[j-1] or p[j-1] == "?") and dp[i-1][j-1]
    return dp[m][n]

print isMatch("c", "*?*")
print isMatch("aa", "a")
print isMatch("aaa", "aa")
print isMatch("aab", "c*a*b")
print isMatch("aa", "*")
print isMatch("aa", "aa")
print isMatch("ab", "a*")
print isMatch("ab", "?*")
