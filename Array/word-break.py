#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-07 16:48:48
# File Name: word-break.py
# Description: 单词拆分 I Word Break 
# LintCode: https://www.lintcode.com/problem/word-break/
#########################################################################
def wordBreak(s, dict):
    n = len(s)
    if n == 0:
        return True

    max_len = 0
    for word in dict:
        max_len = max(len(word), max_len)

    if max_len == 0:
        return False
    
    import Queue
    queue = Queue.Queue()
    queue.put(0)

    visited = set()
    visited.add(0)

    while not queue.empty(): 
        left = queue.get()
        for right in range(left+1,  min(left+1+max_len, n+1)):
            if right in visited: 
                continue

            if s[left:right] in dict:
                if right == n:
                    return True

                queue.put(right)
                visited.add(right)
    return False



s = "lintcode"
dict = ["lint","code"]
print wordBreak(s, dict)
