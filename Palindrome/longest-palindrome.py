#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-14 15:28:39
# File Name: longest-palindrome.py
# Description: 最长回文串长度
# LintCode: https://www.lintcode.com/problem/longest-palindrome/ 
#########################################################################
def longestPalindrome(s):
    if not s or len(s) == 0:
        return 0

    max_len = 0
    char_map = {}
    for char in s:
        if char not in char_map:
            char_map[char] = 1
        else:
            char_map.pop(char)
            max_len += 2

    if len(char_map) > 0:
        max_len += 1

    return max_len


s = "abccccdd"
print longestPalindrome(s)
