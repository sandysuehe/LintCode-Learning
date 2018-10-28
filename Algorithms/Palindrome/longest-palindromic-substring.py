#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-14 15:28:39
# File Name: longest-palindromic-substring.py
# Description: 最长回文子串
# LintCode: https://www.lintcode.com/problem/longest-palindromic-substring/ 
#########################################################################
# 思路: 找回文字串的问题，就要以每一个字符为中心，像两边扩散来寻找回文串，这个算法的时间复杂度是O(n*n)
# 对于奇数情况的回文子串，我们就从遍历到的位置为中心，向两边进行扩散;
# 对于偶数情况的回文子串，我们就把当前位置和下一个位置当作偶数行回文的最中间两个字符，然后向两边进行搜索
########################################################################
def longestPalindrome(s):
    n = len(s)
    if n < 2:
        return s
    max_len = 0
    start = 0

    for i in range(0, n-1):
        # 对于奇数情况的回文子串，我们就从遍历到的位置为中心，向两边进行扩散;
        start, max_len = searchPalindrome(s, i, i, start, max_len)   
        # 对于偶数情况的回文子串，我们就把当前位置和下一个位置当作偶数行回文的最中间两个字符，然后向两边进行搜索
        start, max_len = searchPalindrome(s, i, i+1, start, max_len) 
    return s[start: start+max_len]

def searchPalindrome(s, left, right, start, max_len):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1

    new_len = (right-1)-(left+1)+1
    if max_len < new_len:
        start = left + 1
        max_len = new_len 
    return start, max_len

# s = "abcdzdcab"
s = "ccd"
print longestPalindrome(s)
