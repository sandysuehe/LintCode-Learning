#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-17 17:00:21
# File Name: longest-substring-without-repeating-characters.py
# Description: 最长无重复字符的子串 Longest Substring Without Repeating Characters 
# LintCode: https://www.lintcode.com/problem/longest-substring-without-repeating-characters/
#########################################################################
def lengthOfLongestSubstring(s):
    uniq_chars = set()
    n = len(s)
    ans = 0
    j = 0

    for i in range(n):
        while j < n and s[j] not in uniq_chars:
            uniq_chars.add(s[j])
            j += 1
        ans = max(ans, j-i)
        uniq_chars.remove(s[i])

    return ans

s = "abcabcbb"
print lengthOfLongestSubstring(s)
