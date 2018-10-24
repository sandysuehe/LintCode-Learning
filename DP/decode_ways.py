#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-10-16 19:16:09
# File Name: decode_ways.py
# Description: decode_way 
# LintCode: https://www.lintcode.com/problem/decode-ways/
#########################################################################
def numDecodings(s):
    if not s or int(s[0]) == 0:
        return 0

    n = len(s)
    dp = [1] * (n+1)

    for i in range(2, n+1):
        own_num = int(s[i-1])
        two_num = int(s[i-2])*10 + int(s[i-1]) 
        if two_num in (10, 20):
            dp[i] = dp[i-2]
        elif two_num > 10 and two_num <=26:
            dp[i] = dp[i-2] + dp[i-1]
        elif own_num != 0:
            dp[i] = dp[i-1]
        else:
            return 0
    return dp[n]

print numDecodings("12")
print numDecodings("192611")
