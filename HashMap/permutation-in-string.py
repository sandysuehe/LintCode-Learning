#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-10-16 15:42:06
# File Name: permutation-in-string.py
# Description: Permutation in String 
# LintCode: https://www.lintcode.com/problem/permutation-in-string/
# 思路: Sliding Window
#########################################################################
def checkInclusion(s1, s2):
    if not s1 or not s2:
        return False

    hash_map = {}
    for char in s1:
        hash_map[char] = hash_map.get(char, 0) + 1
    
    count = len(hash_map)
    n1 = len(s1)
    n2 = len(s2)

    start = 0
    end = 0

    # sliding window
    while end < n2:
        end_char = s2[end]
        if end_char in hash_map:
            # s2中的字符end_char也在在s1, hash_map[end_char]--
            hash_map[end_char] = hash_map[end_char] - 1

            if hash_map.get(end_char) == 0:
                # hash_map中的end_char已被使用完
                count -= 1
        end += 1

        while count == 0:
            if end - start == n1:
                return True
            # 如果start->end长度不等于n1，即需要移动窗口左边界
            start_char = s2[start]
            if start_char in hash_map:
                hash_map[start_char] = hash_map[start_char] + 1
                if hash_map.get(start_char) > 0:
                    count += 1
            start += 1

    return False

s1 = "ab"
s2 = "eidbaooo"
s2 = "eidboaoo"
print checkInclusion(s1, s2)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
