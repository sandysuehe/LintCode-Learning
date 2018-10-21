def firstUniqChar(s):
#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-22 13:11:51
# File Name: first-unique-character-in-a-string.py
# Description: 第一个只出现一次的字符
# LintCode: https://www.lintcode.com/problem/first-unique-character-in-a-string/
#########################################################################
    hash_map = {}
    for i in s:
        if i not in hash_map:
            hash_map[i] = 1
        else:
            hash_map[i] += 1

    for i in s:
        if hash_map[i] == 1:
            return s.index(i)
    return -1
    
#s = "lintcode" 
s = "lovelintcode"
s = ""
s = "aa"
print firstUniqChar(s)
