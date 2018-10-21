#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-15 17:43:43
# File Name: minWindow.py
# Description: Minimum Window Substring 最小窗口子串 
# LintCode: https://www.lintcode.com/problem/minimum-window-substring/
#########################################################################
def minWindow(source, target):
    if len(target) > len(source):
        return ""
    res = ""
    hash_set = {}

    # 遍历target字符串，存放在hash_set里
    for i in range(0, len(target)):
        if target[i] not in hash_set:
            hash_set[target[i]] = 1
        else:
            hash_set[target[i]] += 1

    left = 0
    count = 0 # 窗口大小count
    min_len = len(source) + 1

    # 遍历source字符串
    for right in range(0, len(source)):
        # 如果source中的字符在hash_set中，则hash_set中对应的val减1
        if source[right] in hash_set:
            hash_set[source[right]] -= 1
            # 如果hash_set中对应的val减1后，仍然不小于0，则窗口大小加1
            if hash_set[source[right]] >= 0:
                count += 1
            while count == len(target):
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    res = source[left:left+min_len]
                # while循环里要移动left，所以这里需要把hash_set里的val加1
                if source[left] in hash_set:
                    hash_set[source[left]] += 1
                    # 如果移动left后，hash_set里的source[left] >=1
                    # 说明窗口里缺少里source[left]元素, count需要减1
                    if hash_set[source[left]] > 0:
                        count -= 1
                left += 1
    return res
    
source = "ADOBECODEBANC"
target = "ABC"
print minWindow(source, target)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
