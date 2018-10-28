#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-17 17:00:21
# File Name: repeated-dna.py
# Description:  重复 Repeated DNA 
# LintCode: https://www.lintcode.com/problem/repeated-dna/
#########################################################################
# 思路:
# 使用dict，遍历整个string，然后存储所有10个字符的子串到dict中，key存放字符串出现的次数。
# 遍历dict，找到所有满足条件的子串，即key>1, 将对应的string append到result中，return即可
#########################################################################
def findRepeatedDna(s):
    ans = []
    hash_map = {}
    n = len(s)

    for i in range(n-9):
        key = s[i:i+10]
        hash_map[key] = hash_map.get(key, 0) + 1

    for key in hash_map:
        if hash_map[key] > 1:
            ans.append(key)
    return ans

s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print findRepeatedDna(s)
